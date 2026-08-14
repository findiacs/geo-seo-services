
import sys
from unittest.mock import MagicMock
from pathlib import Path

# Mock flask before importing app
mock_flask = MagicMock()
sys.modules["flask"] = mock_flask

import scripts.webapp.app as app

def test_list_pdfs(tmp_path):
    # Setup
    proposals_dir = tmp_path / "proposals"
    proposals_dir.mkdir()
    (proposals_dir / "test1.pdf").touch()
    (proposals_dir / "test2.pdf").touch()
    (proposals_dir / "not_a_pdf.txt").touch()

    app.PROPOSALS_DIR = proposals_dir

    # Test
    pdfs = app.list_pdfs()

    assert len(pdfs) == 2
    assert pdfs[0].name == "test2.pdf"
    assert pdfs[1].name == "test1.pdf"

def test_find_pdf_with_preloaded(tmp_path):
    # Setup
    proposals_dir = tmp_path / "proposals"
    proposals_dir.mkdir()
    pdf1 = proposals_dir / "example.com-prop.pdf"
    pdf1.touch()

    app.PROPOSALS_DIR = proposals_dir
    all_pdfs = [pdf1]

    # Test
    prospect = {"domain": "example.com"}
    found = app.find_pdf(prospect, all_pdfs=all_pdfs)
    assert found == pdf1

    # Test not found
    prospect2 = {"domain": "other.com"}
    found2 = app.find_pdf(prospect2, all_pdfs=all_pdfs)
    assert found2 is None

def test_find_pdf_fallback(tmp_path):
    # Setup
    proposals_dir = tmp_path / "proposals"
    proposals_dir.mkdir()
    pdf1 = proposals_dir / "example.com-prop.pdf"
    pdf1.touch()

    app.PROPOSALS_DIR = proposals_dir

    # Test
    prospect = {"domain": "example.com"}
    found = app.find_pdf(prospect)
    assert found == pdf1

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
