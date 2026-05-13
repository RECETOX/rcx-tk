from click.testing import CliRunner
from rcx_tk import __main__


def test_sequence_subcommand_dispatches(monkeypatch):
    called = {}

    def fake_process_sequence_file(file_path, out_path):
        called["args"] = (file_path, out_path)

    monkeypatch.setattr(__main__, "process_sequence_file", fake_process_sequence_file)

    runner = CliRunner()
    result = runner.invoke(__main__.main, ["sequence", "in.tsv", "out.tsv"])

    assert result.exit_code == 0
    assert called["args"] == ("in.tsv", "out.tsv")


def test_alkanes_subcommand_dispatches(monkeypatch):
    called = {}

    def fake_process_alkane_file(file_path, out_path):
        called["args"] = (file_path, out_path)

    monkeypatch.setattr(__main__, "process_alkane_file", fake_process_alkane_file)

    runner = CliRunner()
    result = runner.invoke(__main__.main, ["alkanes", "in.txt", "out.tsv"])

    assert result.exit_code == 0
    assert called["args"] == ("in.txt", "out.tsv")


def test_msdial_subcommand_dispatches_with_explicit_mz_tol(monkeypatch):
    called = {}

    def fake_process_msdial_file(file_path, out_path, mz_tol_ppm):
        called["args"] = (file_path, out_path, mz_tol_ppm)

    monkeypatch.setattr(__main__, "process_msdial_file", fake_process_msdial_file)

    runner = CliRunner()
    result = runner.invoke(__main__.main, ["msdial", "in.tsv", "out.tsv", "10"])

    assert result.exit_code == 0
    assert called["args"] == ("in.tsv", "out.tsv", 10)


def test_msdial_subcommand_uses_default_mz_tol(monkeypatch):
    called = {}

    def fake_process_msdial_file(file_path, out_path, mz_tol_ppm):
        called["args"] = (file_path, out_path, mz_tol_ppm)

    monkeypatch.setattr(__main__, "process_msdial_file", fake_process_msdial_file)

    runner = CliRunner()
    result = runner.invoke(__main__.main, ["msdial", "in.tsv", "out.tsv"])

    assert result.exit_code == 0
    assert called["args"] == ("in.tsv", "out.tsv", 5)
