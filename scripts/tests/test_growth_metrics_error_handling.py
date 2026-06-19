#!/usr/bin/env python3
"""
Unit tests for growth-metrics.py error handling system.

Tests the error classification logic and retry behavior to ensure
robust error handling and proper transient vs permanent error distinction.
"""

from __future__ import annotations

import pytest
import requests
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import sys
import importlib.util

# Get parent directory and add to path
parent_dir = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(parent_dir))

# Mock logging before importing growth_metrics to avoid file creation issues
with patch('logging.FileHandler'):
    # Import from the actual file (not a module)
    spec = importlib.util.spec_from_file_location("growth_metrics", parent_dir / "growth-metrics.py")
    growth_metrics = importlib.util.module_from_spec(spec)

    # Mock the logging configuration
    with patch('logging.basicConfig'):
        spec.loader.exec_module(growth_metrics)

classify_error = growth_metrics.classify_error
ErrorType = growth_metrics.ErrorType
MAX_RETRIES = growth_metrics.MAX_RETRIES
RETRY_DELAY = growth_metrics.RETRY_DELAY


class TestErrorClassification:
    """Test error classification system."""

    def test_timeout_is_transient(self):
        """Timeout errors should be classified as transient."""
        exc = requests.Timeout()
        assert classify_error(exc) == ErrorType.TRANSIENT

    def test_connection_error_is_transient(self):
        """Connection errors should be classified as transient."""
        exc = requests.ConnectionError()
        assert classify_error(exc) == ErrorType.TRANSIENT

    def test_5xx_server_errors_are_transient(self):
        """5xx server errors should be classified as transient (retry-able)."""
        # Create mock HTTPError with 500 status code
        exc = requests.HTTPError()
        exc.response = Mock()
        exc.response.status_code = 500
        assert classify_error(exc) == ErrorType.TRANSIENT

        exc.response.status_code = 503
        assert classify_error(exc) == ErrorType.TRANSIENT

        exc.response.status_code = 599
        assert classify_error(exc) == ErrorType.TRANSIENT

    def test_4xx_client_errors_are_permanent(self):
        """4xx client errors should be classified as permanent (no retry)."""
        # Create mock HTTPError with 400 status code
        exc = requests.HTTPError()
        exc.response = Mock()
        exc.response.status_code = 400
        assert classify_error(exc) == ErrorType.PERMANENT

        exc.response.status_code = 403
        assert classify_error(exc) == ErrorType.PERMANENT

        exc.response.status_code = 404
        assert classify_error(exc) == ErrorType.PERMANENT

    def test_unknown_errors_are_unknown(self):
        """Errors without clear classification should be unknown."""
        exc = requests.RequestException()
        assert classify_error(exc) == ErrorType.UNKNOWN

    def test_http_error_without_response_is_unknown(self):
        """HTTPError without response object should be unknown."""
        exc = requests.HTTPError()
        # No response object attached
        assert classify_error(exc) == ErrorType.UNKNOWN


class TestExponentialBackoff:
    """Test exponential backoff retry logic."""

    @patch('time.sleep')
    @patch('requests.get')
    def test_exponential_backoff_timing(self, mock_get, mock_sleep):
        """Verify exponential backoff timing: RETRY_DELAY * (2 ** attempt)."""
        # Configure mock to raise timeout errors
        mock_get.side_effect = requests.Timeout("Connection timeout")

        # Should retry MAX_RETRIES times with exponential backoff
        result = growth_metrics.honcho_get("/test/endpoint")

        # Should return None after all retries exhausted
        assert result is None

        # Verify sleep was called with exponential backoff
        expected_sleep_calls = MAX_RETRIES - 1
        assert mock_sleep.call_count == expected_sleep_calls

        # Check exponential backoff: RETRY_DELAY * (2 ** attempt)
        for i in range(expected_sleep_calls):
            expected_sleep = RETRY_DELAY * (2 ** i)
            mock_sleep.assert_any_call(expected_sleep)

    @patch('time.sleep')
    @patch('requests.get')
    def test_permanent_error_no_retry(self, mock_get, mock_sleep):
        """Permanent errors should not retry."""
        # Create mock HTTPError with 404 status code (permanent)
        exc = requests.HTTPError()
        exc.response = Mock()
        exc.response.status_code = 404
        mock_get.side_effect = exc

        result = growth_metrics.honcho_get("/test/endpoint")

        # Should return None immediately without retry
        assert result is None

        # Should not sleep (no retry for permanent errors)
        assert mock_sleep.call_count == 0

    @patch('time.sleep')
    @patch('requests.get')
    def test_transient_error_retries_until_success(self, mock_get, mock_sleep):
        """Transient errors should retry until success."""
        # Mock to fail twice, then succeed
        mock_response = Mock()
        mock_response.json.return_value = {"success": True}
        mock_get.side_effect = [
            requests.Timeout("First timeout"),
            requests.Timeout("Second timeout"),
            mock_response
        ]

        result = growth_metrics.honcho_get("/test/endpoint")

        # Should succeed after retries
        assert result == {"success": True}

        # Should have slept twice (for the two failures)
        assert mock_sleep.call_count == 2


class TestErrorTracking:
    """Test error tracking and logging."""

    def setup_method(self):
        """Clear API_ERRORS before each test."""
        # Clear the global API_ERRORS list
        if hasattr(growth_metrics, 'API_ERRORS'):
            growth_metrics.API_ERRORS.clear()

    @patch('logging.Logger.error')
    @patch('requests.get')
    def test_permanent_error_logged_properly(self, mock_get, mock_logger):
        """Permanent errors should be logged with proper context."""
        exc = requests.HTTPError()
        exc.response = Mock()
        exc.response.status_code = 404
        mock_get.side_effect = exc

        honcho_get = growth_metrics.honcho_get
        API_ERRORS = growth_metrics.API_ERRORS

        result = honcho_get("/test/endpoint")

        # Should log the error
        assert mock_logger.called
        assert result is None

        # Should track error with metadata
        assert len(API_ERRORS) == 1
        error_entry = API_ERRORS[0]
        assert error_entry["method"] == "GET"
        assert error_entry["path"] == "/test/endpoint"
        assert error_entry["error_type"] == ErrorType.PERMANENT
        assert error_entry["attempts"] == 1  # No retry for permanent errors


class TestErrorTypeConstants:
    """Test error type constants are properly defined."""

    def test_error_type_constants(self):
        """Verify error type constants are correctly defined."""
        assert ErrorType.TRANSIENT == "transient"
        assert ErrorType.PERMANENT == "permanent"
        assert ErrorType.UNKNOWN == "unknown"

    def test_retry_configuration_constants(self):
        """Verify retry configuration constants are reasonable."""
        assert MAX_RETRIES > 0
        assert RETRY_DELAY > 0
        assert isinstance(MAX_RETRIES, int)
        assert isinstance(RETRY_DELAY, (int, float))


if __name__ == "__main__":
    # Run tests
    pytest.main([__file__, "-v", "--tb=short"])
