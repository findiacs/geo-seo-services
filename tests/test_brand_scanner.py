import sys
import os
from unittest.mock import MagicMock, patch
import pytest
from urllib.parse import quote_plus

# Ensure scripts/ is importable from the worktree
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

with patch.dict('sys.modules', {
    'requests': MagicMock(),
    'bs4': MagicMock(),
    'beautifulsoup4': MagicMock()
}):
    from brand_scanner import check_reddit_presence


def test_check_reddit_presence_simple_brand():
    result = check_reddit_presence("Acme")

    assert result["platform"] == "Reddit"
    assert result["correlation"] == "High"
    assert result["weight"] == "25%"
    assert result["has_subreddit"] is False
    assert result["mentioned_in_discussions"] is False
    assert result["search_url"] == "https://www.reddit.com/search/?q=Acme"

    # Check instructions exist and are a list
    assert "check_instructions" in result
    assert isinstance(result["check_instructions"], list)
    assert len(result["check_instructions"]) > 0
    assert "Acme" in result["check_instructions"][0]

    # Check recommendations exist and are a list
    assert "recommendations" in result
    assert isinstance(result["recommendations"], list)
    assert len(result["recommendations"]) > 0


def test_check_reddit_presence_spaced_brand():
    result = check_reddit_presence("Acme Corporation")

    # Check URL encoding for space
    assert result["search_url"] == "https://www.reddit.com/search/?q=Acme+Corporation"
    assert "Acme Corporation" in result["check_instructions"][0]


def test_check_reddit_presence_special_characters():
    result = check_reddit_presence("O'Reilly & Sons")

    # Check URL encoding for special characters
    # quote_plus for "O'Reilly & Sons" -> "O%27Reilly+%26+Sons"
    assert result["search_url"] == "https://www.reddit.com/search/?q=O%27Reilly+%26+Sons"


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

def test_check_reddit_presence_special_characters_main():
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
