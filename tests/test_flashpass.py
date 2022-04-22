"""FlashPass tests module."""
from flashpass import __version__


def test_version():
    """Assert that the version is correct."""
    assert __version__ == "0.1.3"
