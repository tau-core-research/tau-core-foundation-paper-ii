from pathlib import Path
import json
import zipfile


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paperII_submission_source" / "main.tex"


def test_required_files_exist():
    for path in [
        ROOT / "README.md", ROOT / "REVIEWER_READINESS.md",
        ROOT / "CITATION.cff", ROOT / "DATA_NOTICE.md", TEX,
        ROOT / "paperII_submission_source" / "refs.bib",
        ROOT / "paperII_submission_source" / "main.pdf",
        ROOT / "arxiv_submission_source.zip",
    ]:
        assert path.exists(), path


def test_claim_markers():
    text = TEX.read_text()
    for marker in [
        "Technical Paper I (Series Paper II)",
        "Finite source-signature representation uniqueness",
        "Two-sector marginal no-go",
        "Four-sector all-proper-marginal no-go",
        "Onto-incidence faithful-state theorem",
        "Compression of finite joint selection",
        "does not construct or occupy",
        "Later source-completion status",
        "current-reduct counterpair",
    ]:
        assert marker in text


def test_four_qubit_pauli_dimension_ledger():
    weights = [4 * 3, 6 * 3**2, 4 * 3**3, 3**4]
    assert weights == [12, 54, 108, 81]
    assert sum(weights) == 4**4 - 1 == 255
    assert sum(weights[:3]) == 174
    data = json.loads((ROOT / "data/derived/four_qubit_pauli_dimension_summary.json").read_text())
    assert data["proper_marginal_span"] == 174
    assert data["weight_4_hidden_subspace"] == 81


def test_countermodel_spectra_are_positive():
    for eps in [0.1, -0.2, 0.9]:
        assert (1 + eps) / 16 > 0
        assert (1 - eps) / 16 > 0


def test_figures_and_arxiv_source():
    text = TEX.read_text()
    for name in ["fig_source_signature_pipeline.pdf", "fig_pauli_dimension_audit.pdf"]:
        assert name in text
        assert (ROOT / "paperII_submission_source" / "figures" / name).exists()
    with zipfile.ZipFile(ROOT / "arxiv_submission_source.zip") as archive:
        names = archive.namelist()
    assert "main.tex" in names and "refs.bib" in names
    assert "main.pdf" not in names
    assert all(not name.endswith(".aux") for name in names)
