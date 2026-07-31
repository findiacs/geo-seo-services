import sys
import os
from unittest.mock import patch, MagicMock

# Create mock modules for external dependencies
mock_requests = MagicMock()
mock_bs4 = MagicMock()
sys.modules['requests'] = mock_requests
sys.modules['bs4'] = mock_bs4

# Add scripts to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "scripts")))

import unittest
from llmstxt_generator import generate_llmstxt, validate_llmstxt
from fetch_page import fetch_page
from citability_scorer import analyze_page_citability
from brand_scanner import check_wikipedia_presence

class TestSSRFMitigation(unittest.TestCase):

    @patch('llmstxt_generator.is_safe_url')
    def test_llmstxt_generator_blocks_unsafe(self, mock_is_safe):
        mock_is_safe.return_value = False

        url = "http://169.254.169.254/latest/meta-data/"
        result = generate_llmstxt(url)

        self.assertIn("error", result)
        self.assertIn("Blocked unsafe URL", result["error"])
        # requests.get should not have been called on this mock
        mock_requests.get.assert_not_called()

    @patch('llmstxt_generator.is_safe_url')
    def test_llmstxt_validator_blocks_unsafe(self, mock_is_safe):
        mock_is_safe.return_value = False

        url = "http://localhost/llms.txt"
        result = validate_llmstxt(url)

        self.assertTrue(any("Blocked unsafe URL" in issue for issue in result["issues"]))
        mock_requests.get.assert_not_called()

    @patch('fetch_page.is_safe_url')
    def test_fetch_page_blocks_unsafe(self, mock_is_safe):
        mock_is_safe.return_value = False

        url = "http://127.0.0.1/admin"
        result = fetch_page(url)

        self.assertTrue(any("Blocked unsafe" in err for err in result["errors"]))
        mock_requests.get.assert_not_called()

    @patch('citability_scorer.is_safe_url')
    def test_citability_scorer_blocks_unsafe(self, mock_is_safe):
        mock_is_safe.return_value = False

        url = "http://10.0.0.1/secret"
        result = analyze_page_citability(url)

        self.assertIn("error", result)
        self.assertIn("Blocked unsafe URL", result["error"])
        mock_requests.get.assert_not_called()

    @patch('brand_scanner.is_safe_url')
    def test_brand_scanner_blocks_unsafe(self, mock_is_safe):
        mock_is_safe.return_value = False

        # This will trigger check_wikipedia_presence which uses is_safe_url
        result = check_wikipedia_presence("Malicious Brand")

        # It should return the default result dict without having made any requests
        self.assertFalse(result["has_wikipedia_page"])
        self.assertFalse(result["has_wikidata_entry"])
        mock_requests.get.assert_not_called()

if __name__ == "__main__":
    unittest.main()
