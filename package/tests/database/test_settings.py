"""In this module we test that there is a module settings and is has the required
attributes and functionality"""
from awesome_streamlit.database import settings


def test_github():
    """Test that there is a GITHUB_URL Setting"""
    assert settings.GITHUB_URL


def test_github_raw():
    """Test that there is a GITHUB_RAW_URL Setting"""
    assert settings.GITHUB_RAW_URL
