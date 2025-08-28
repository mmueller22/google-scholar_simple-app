"""Pytest configuration and fixtures for scholar.py tests."""

import os
import sys
from types import ModuleType
from typing import Any, Optional
from unittest.mock import Mock

import pytest

# Add the parent directory to sys.path so we can import scholar
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

scholar: Optional[ModuleType] = None
try:
    import scholar
except ImportError:
    # If import fails, we'll handle it in individual tests
    pass


@pytest.fixture
def mock_response() -> Mock:
    """Mock HTTP response for testing."""
    mock_resp = Mock()
    mock_resp.read.return_value = b"<html><body>Mock response</body></html>"
    mock_resp.getcode.return_value = 200
    return mock_resp


@pytest.fixture
def sample_scholar_html() -> str:
    """Sample Google Scholar HTML response."""
    return """
    <html>
    <body>
        <div class="gs_r gs_or gs_scl">
            <div class="gs_ggs gs_fl">
                <div class="gs_ttss">
                    <a href="http://example.com/paper.pdf">[PDF]</a>
                </div>
            </div>
            <div class="gs_ri">
                <h3 class="gs_rt">
                    <a href="http://example.com/paper">Sample Paper Title</a>
                </h3>
                <div class="gs_a">
                    JA Smith, AB Jones - Journal of Examples, 2023
                </div>
                <div class="gs_rs">
                    This is a sample excerpt from the paper abstract...
                </div>
                <div class="gs_fl">
                    <a href="/scholar?cites=123456">Cited by 42</a>
                    <a href="/scholar?cluster=789012">All 3 versions</a>
                </div>
            </div>
        </div>
    </html>
    """


@pytest.fixture
def scholar_querier() -> Any:
    """Create a ScholarQuerier instance for testing."""
    if scholar is None:
        pytest.skip("Scholar module not available")

    querier = scholar.ScholarQuerier()
    return querier


@pytest.fixture
def scholar_query() -> Any:
    """Create a basic ScholarQuery for testing."""
    if scholar is None:
        pytest.skip("Scholar module not available")

    # Use SearchScholarQuery which has the set_phrase method
    query = scholar.SearchScholarQuery()
    query.set_phrase("machine learning")
    return query


@pytest.fixture
def scholar_article() -> Any:
    """Create a sample ScholarArticle for testing."""
    if scholar is None:
        pytest.skip("Scholar module not available")

    article = scholar.ScholarArticle()
    # Use dictionary-style access instead of set_ methods
    article["title"] = "Sample Paper Title"
    article["url"] = "http://example.com/paper"
    article["year"] = "2023"
    article["num_citations"] = 42
    article["num_versions"] = 3
    return article
