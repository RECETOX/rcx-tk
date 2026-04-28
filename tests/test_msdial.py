import filecmp
import os
import numpy as np
import pandas as pd
import pytest
from rcx_tk import msdial
from rcx_tk.utils import concat_str


@pytest.fixture
def all_duplicates():
    """Fixture to provide indices."""
    return [
        pd.Index([1, 2]),
        pd.Index([2, 3]),
        pd.Index([9]),
    ]


def _index_groups_as_sets(index_groups):
    return {frozenset(idx.tolist()) for idx in index_groups}


def test_aggregations():
    """Build aggregation mapping with mean, concat, and max functions."""
    mean_columns = ["A", "B"]
    concat_columns = ["C"]
    abundance_columns = ["D", "E"]

    actual = msdial.aggregations(mean_columns, concat_columns, abundance_columns)

    assert actual["A"] is np.mean
    assert actual["B"] is np.mean
    assert actual["C"] is concat_str
    assert actual["D"] is np.max
    assert actual["E"] is np.max


def test_find_all_duplicates():
    """Detect duplicate non-zero values per column and return grouped indices."""
    data_matrix = pd.DataFrame(
        {
            "S1": [1.0, 1.0, 2.0, 0.0],
            "S2": [3.0, 4.0, 4.0, 0.0],
        },
        index=["a", "b", "c", "d"],
    )

    actual = msdial.find_all_duplicates(data_matrix)

    assert _index_groups_as_sets(actual) == {frozenset(["a", "b"]), frozenset(["b", "c"])}


def test_find_clusters_transitive_merge(all_duplicates):
    """Merge overlapping duplicate index groups transitively into clusters."""
    actual = msdial.find_clusters(all_duplicates)
    assert _index_groups_as_sets(actual) == {frozenset([1, 2, 3]), frozenset([9])}


def test_get_index_unions_all_duplicate_groups(all_duplicates):
    """Return a union index containing all duplicate-group members."""
    actual = msdial.union(all_duplicates)
    assert set(actual.tolist()) == {1, 2, 3, 9}


def test_process_msdial_merges_duplicate_alignments():
    """Aggregate duplicated alignments and keep non-duplicate rows unchanged."""
    raw = pd.DataFrame(
        {
            "M1": [10.0, 30.0, 50.0],
            "M2": [20.0, 40.0, 60.0],
            "M3": [30.0, 50.0, 70.0],
            101: [5.0, 5.0, 1.0],
            102: [0.0, 7.0, 8.0],
        },
        index=pd.Index([1, 2, 3], name="Alignment ID"),
    )

    actual = msdial.process_msdial(raw, metadata_cols=3, index_col="Alignment ID")

    assert 1 not in actual.index
    assert 2 not in actual.index
    assert "1,2" in actual.index
    assert actual.loc["1,2", "M1"] == 20.0
    assert actual.loc["1,2", "M2"] == 30.0
    assert actual.loc["1,2", "M3"] == 40.0
    assert actual.loc["1,2", 101] == 5.0
    assert actual.loc["1,2", 102] == 7.0


def test_integration(tmpdir):
    """Test on real MSDial outputs."""
    inpath = os.path.join("tests", "test_data", "msdial_katka.tsv")
    outpath = tmpdir / "result.tsv"
    msdial.process_msdial_file(inpath, outpath)

    expected = os.path.join("tests", "test_data", "msdial_katka_corrected.tsv")
    assert filecmp.cmp(outpath, expected)
