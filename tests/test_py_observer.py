"""Tests for py-observer."""

import pytest
from py_observer import observer


class TestObserver:
    """Test suite for observer."""

    def test_basic(self):
        """Test basic usage."""
        result = observer("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            observer("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = observer(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
