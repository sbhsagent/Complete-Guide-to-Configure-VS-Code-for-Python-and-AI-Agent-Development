"""
Tests for AI Agent Development Package
"""
import pytest


def test_import_src():
    """Test that the src package can be imported"""
    import src

    assert src.__version__ == "1.0.0"


def test_basic_math():
    """Basic test to ensure pytest is working"""
    assert 1 + 1 == 2


def test_environment_setup():
    """Test that basic Python environment is set up correctly"""
    import sys

    assert sys.version_info >= (3, 11)
