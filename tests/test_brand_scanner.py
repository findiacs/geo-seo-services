import sys
from unittest.mock import MagicMock

# Mocking modules that are not installed in the environment
mock_requests = MagicMock()
mock_bs4 = MagicMock()

sys.modules["requests"] = mock_requests
sys.modules["bs4"] = mock_bs4

import os
import pytest
from urllib.parse import quote_plus

# Ensure scripts/ is importable from the worktree
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from brand_scanner import check_reddit_presence

def test_check_reddit_presence_structure():
    brand_name = "Test Brand"
    result = check_reddit_presence(brand_name)

    assert result["platform"] == "Reddit"
    assert result["correlation"] == "High"
    assert result["weight"] == "25%"
    assert result["has_subreddit"] is False
    assert result["mentioned_in_discussions"] is False
    assert result["search_url"] == f"https://www.reddit.com/search/?q={quote_plus(brand_name)}"
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) > 0
    assert isinstance(result["check_instructions"], list)
    assert len(result["check_instructions"]) > 0
    assert brand_name in result["check_instructions"][0]

def test_check_reddit_presence_special_characters():
    brand_name = "AT&T / Verizon"
    result = check_reddit_presence(brand_name)

    expected_url = f"https://www.reddit.com/search/?q={quote_plus(brand_name)}"
    assert result["search_url"] == expected_url
    assert brand_name in result["check_instructions"][0]

def test_check_reddit_presence_empty_name():
    brand_name = ""
    result = check_reddit_presence(brand_name)
    assert result["search_url"] == "https://www.reddit.com/search/?q="
    assert "''" in result["check_instructions"][0]
