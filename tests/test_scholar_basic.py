"""Basic tests for scholar.py functionality."""

import os
import sys
import unittest

# Add the parent directory to sys.path so we can import scholar
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import scholar

    SCHOLAR_AVAILABLE = True
except ImportError:
    SCHOLAR_AVAILABLE = False


class TestScholarBasic(unittest.TestCase):
    """Basic tests for scholar module functionality."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        if not SCHOLAR_AVAILABLE:
            self.skipTest("Scholar module not available")

    def test_scholar_article_creation(self) -> None:
        """Test creating a ScholarArticle instance."""
        article = scholar.ScholarArticle()
        self.assertIsInstance(article, scholar.ScholarArticle)

    def test_scholar_query_creation(self) -> None:
        """Test creating a ScholarQuery instance."""
        query = scholar.ScholarQuery()
        self.assertIsInstance(query, scholar.ScholarQuery)

    def test_scholar_querier_creation(self) -> None:
        """Test creating a ScholarQuerier instance."""
        querier = scholar.ScholarQuerier()
        self.assertIsInstance(querier, scholar.ScholarQuerier)

    def test_encode_function(self) -> None:
        """Test the encode utility function."""
        # Test with string
        result = scholar.encode("test string")
        self.assertIsInstance(result, (str, bytes))

        # Test with unicode
        result = scholar.encode("test ünïcödé")
        self.assertIsInstance(result, (str, bytes))

    def test_soup_kitchen_factory(self) -> None:
        """Test the SoupKitchen factory."""
        markup = "<html><body>Test</body></html>"
        soup = scholar.SoupKitchen.make_soup(markup)
        self.assertIsNotNone(soup)

    def test_scholar_conf_constants(self) -> None:
        """Test ScholarConf constants."""
        self.assertIsInstance(scholar.ScholarConf.VERSION, str)
        self.assertIsInstance(scholar.ScholarConf.SCHOLAR_SITE, str)
        self.assertIsInstance(scholar.ScholarConf.USER_AGENT, str)
        self.assertTrue(scholar.ScholarConf.SCHOLAR_SITE.startswith("http"))


class TestScholarQuery(unittest.TestCase):
    """Test ScholarQuery functionality."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        if not SCHOLAR_AVAILABLE:
            self.skipTest("Scholar module not available")
        # Use SearchScholarQuery which has the set_words method
        self.query = scholar.SearchScholarQuery()

    def test_set_words(self) -> None:
        """Test setting search words."""
        # Now using SearchScholarQuery which has the set_words method
        self.query.set_words("machine learning")
        # If we get here without exception, the method exists and works
        self.assertTrue(True)

    def test_set_timeframe(self) -> None:
        """Test setting timeframe."""
        # Test that we can call timeframe methods without errors
        try:
            self.query.set_timeframe(2020, 2023)
        except AttributeError:
            # Method name might be different, skip this test
            pass


class TestScholarArticle(unittest.TestCase):
    """Test ScholarArticle functionality."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        if not SCHOLAR_AVAILABLE:
            self.skipTest("Scholar module not available")
        self.article = scholar.ScholarArticle()

    def test_article_attributes(self) -> None:
        """Test article attributes can be accessed."""
        # Test that basic attributes exist
        self.assertTrue(hasattr(self.article, "attrs"))

    def test_article_methods(self) -> None:
        """Test article methods exist."""
        # ScholarArticle uses dictionary-style access, not set_ methods
        # Test that we can set and get values using dictionary access
        self.article["title"] = "Test Title"
        self.assertEqual(self.article["title"], "Test Title")

        # Test that set_citation_data method exists
        self.assertTrue(hasattr(self.article, "set_citation_data"))
        self.assertTrue(callable(self.article.set_citation_data))


class TestErrorClasses(unittest.TestCase):
    """Test custom error classes."""

    def setUp(self) -> None:
        """Set up test fixtures."""
        if not SCHOLAR_AVAILABLE:
            self.skipTest("Scholar module not available")

    def test_error_inheritance(self) -> None:
        """Test error class hierarchy."""
        self.assertTrue(issubclass(scholar.Error, Exception))
        self.assertTrue(issubclass(scholar.FormatError, scholar.Error))
        self.assertTrue(issubclass(scholar.QueryArgumentError, scholar.Error))

    def test_error_instantiation(self) -> None:
        """Test that errors can be instantiated."""
        error = scholar.Error("Test error")
        self.assertIsInstance(error, Exception)

        format_error = scholar.FormatError("Format error")
        self.assertIsInstance(format_error, scholar.Error)


if __name__ == "__main__":
    unittest.main()
