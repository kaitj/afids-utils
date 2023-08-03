from __future__ import annotations

import csv
import json
import tempfile
from os import PathLike, remove
from pathlib import Path

import numpy as np
import pytest
from hypothesis import HealthCheck, assume, given, settings
from hypothesis import strategies as st
from numpy.typing import NDArray

from afids_utils.exceptions import InvalidFiducialNumberError
from afids_utils.io import (
    EXPECTED_DESCS,
    FCSV_FIELDNAMES,
    afids_to_fcsv,
    afids_to_json,
    get_afid,
)
from afids_utils.tests.strategies import afid_coords


@pytest.fixture
def valid_fcsv_file() -> PathLike[str]:
    return (
        Path(__file__).parent / "data" / "tpl-MNI152NLin2009cAsym_afids.fcsv"
    )


@pytest.fixture
def valid_json_file() -> PathLike[str]:
    return (
        Path(__file__).parent / "data" / "tpl-MNI152NLin2009cAsym_afids.json"
    )


class TestGetAfidFcsv:
    @given(afid_num=st.integers(min_value=1, max_value=32))
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_valid_fcsv_get_afid(
        self, valid_fcsv_file: PathLike[str], afid_num: int
    ) -> None:
        afid = get_afid(valid_fcsv_file, afid_num)

        # Check array type
        assert isinstance(afid, np.ndarray)
        # Check array values
        assert afid.dtype == np.single

    @given(afid_num=st.integers(min_value=-1000, max_value=1000))
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_invalid_fcsv_get_afid(
        self,
        valid_fcsv_file: PathLike[str],
        afid_num: int,
    ) -> None:
        assume(afid_num < 1 or afid_num > 32)

        with pytest.raises(
            InvalidFiducialNumberError, match=".*is not valid."
        ):
            get_afid(valid_fcsv_file, afid_num)

    @given(
        afid_num=st.integers(min_value=1, max_value=32),
        desc=st.text(
            min_size=2,
            max_size=5,
            alphabet=st.characters(whitelist_categories=("L")),
        ),
    )
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_mismatch_desc_fcsv(
        self, valid_fcsv_file: PathLike[str], afid_num: int, desc: str
    ) -> None:
        assume(desc not in EXPECTED_DESCS[afid_num - 1])

        # Replace valid description with a mismatch
        with open(valid_fcsv_file, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(EXPECTED_DESCS[afid_num - 1][0], desc)

        # Write to temp file
        with tempfile.NamedTemporaryFile(
            mode="w",
            prefix="sub-test_desc-",
            suffix="_afids.fcsv",
        ) as out_fcsv_file:
            out_fcsv_file.write(content)
            out_fcsv_file.flush()

            # Test for validity
            with pytest.raises(
                ValueError, match=".*does not match expected*."
            ):
                get_afid(out_fcsv_file.name, afid_num)

    @given(
        afid_num=st.integers(min_value=1, max_value=32),
        ext=st.text(
            min_size=2,
            max_size=5,
            alphabet=st.characters(whitelist_categories=("L")),
        ),
    )
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_invalid_extension_fcsv(
        self, valid_fcsv_file: PathLike[str], afid_num: int, ext: str
    ) -> None:
        assume(not ext == "fcsv" or not ext == "json")
        invalid_file_ext = valid_fcsv_file.with_suffix(f".{ext}")

        with pytest.raises(IOError, match="Invalid file extension"):
            get_afid(invalid_file_ext, afid_num)


class TestGetAfidJson:
    @given(afid_num=st.integers(min_value=1, max_value=32))
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_valid_json_get_afid(
        self, valid_json_file: PathLike[str], afid_num: int
    ) -> None:
        afid = get_afid(valid_json_file, afid_num)

        # Check array type
        assert isinstance(afid, np.ndarray)
        # Check array values
        assert afid.dtype == np.single

    @given(afid_num=st.integers(min_value=-1000, max_value=1000))
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_invalid_json_get_afid(
        self,
        valid_json_file: PathLike[str],
        afid_num: int,
    ) -> None:
        assume(afid_num < 1 or afid_num > 32)

        with pytest.raises(
            InvalidFiducialNumberError, match="Invalid fiducial number*."
        ):
            get_afid(valid_json_file, afid_num)

    @given(
        afid_num=st.integers(min_value=1, max_value=32),
        desc=st.text(
            min_size=2,
            max_size=5,
            alphabet=st.characters(whitelist_categories=("L")),
        ),
    )
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_mismatch_desc_json(
        self, valid_json_file: PathLike[str], afid_num: int, desc: str
    ) -> None:
        assume(desc not in EXPECTED_DESCS[afid_num - 1])

        # Replace valid description with a mismatch
        with open(valid_json_file, "r", encoding="utf-8") as f:
            content = json.load(f)
        content["markups"][0]["controlPoints"][afid_num - 1][
            "description"
        ] = desc

        # Write to temp file
        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            prefix="sub-test_desc-",
            suffix="_afids.json",
        ) as out_json_file:
            json.dump(content, out_json_file, indent=4)
            out_file_path = out_json_file.name

        # Test for validity
        # Needs to be outside of context, otherwise JSONDecodeError thrown
        with pytest.raises(
            ValueError, match=".*does not match expected description"
        ):
            get_afid(out_file_path, afid_num)

        remove(out_file_path)

    @given(
        afid_num=st.integers(min_value=1, max_value=32),
        ext=st.text(
            min_size=2,
            max_size=5,
            alphabet=st.characters(whitelist_categories=("L")),
        ),
    )
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_invalid_extension_json(
        self, valid_json_file: PathLike[str], afid_num: int, ext: str
    ) -> None:
        assume(not ext == "fcsv" or not ext == "json")
        invalid_file_ext = valid_json_file.with_suffix(f".{ext}")

        with pytest.raises(IOError, match="Invalid file extension"):
            get_afid(invalid_file_ext, afid_num)


class TestAfidsToFcsv:
    @given(afids_coords=afid_coords())
    def test_invalid_fcsv_template(
        self, afids_coords: NDArray[np.single]
    ) -> None:
        with pytest.raises(FileNotFoundError):
            afids_to_fcsv(
                afids_coords,
                "/invalid/fcsv/path",
            )

    @given(afids_coords=afid_coords())
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_write_fcsv(
        self, afids_coords: NDArray[np.single], valid_fcsv_file: PathLike[str]
    ) -> None:
        with tempfile.NamedTemporaryFile(
            mode="w", prefix="sub-test_desc-", suffix="_afids.fcsv"
        ) as out_fcsv_file:
            # Create and check output file
            afids_to_fcsv(afids_coords, out_fcsv_file.name)

            # Load files
            with open(
                valid_fcsv_file, "r", encoding="utf-8", newline=""
            ) as template_fcsv_file, open(
                out_fcsv_file.name, "r", encoding="utf-8", newline=""
            ) as output_fcsv_file:
                template_header = [
                    template_fcsv_file.readline() for _ in range(3)
                ]
                output_header = [output_fcsv_file.readline() for _ in range(3)]
                reader = csv.DictReader(
                    output_fcsv_file, fieldnames=FCSV_FIELDNAMES
                )
                output_fcsv = list(reader)

            # Check header
            assert output_header == template_header
            # Check contents
            for idx, row in enumerate(output_fcsv):
                assert (row["x"], row["y"], row["z"]) == (
                    str(afids_coords[idx][0]),
                    str(afids_coords[idx][1]),
                    str(afids_coords[idx][2]),
                )


class TestAfidsToJson:
    @given(afids_coords=afid_coords())
    def test_invalid_json_template(
        self, afids_coords: NDArray[np.single]
    ) -> None:
        with pytest.raises(FileNotFoundError):
            afids_to_json(
                afids_coords,
                "/invalid/json/path",
            )

    @given(afids_coords=afid_coords())
    @settings(
        suppress_health_check=[HealthCheck.function_scoped_fixture],
    )
    def test_write_json(
        self, afids_coords: NDArray[np.single], valid_json_file: PathLike[str]
    ) -> None:
        with tempfile.NamedTemporaryFile(
            mode="w",
            delete=False,
            prefix="sub-test_desc-",
            suffix="_afids.json",
        ) as out_json_file:
            out_json_fpath = out_json_file.name
            afids_to_json(afids_coords, out_json_fpath)

            # Check file was created
            assert Path(out_json_fpath).exists()

        # Check afids positions
        with open(out_json_fpath, "r", encoding="utf-8") as f:
            content = json.load(f)
            for idx in range(afids_coords.shape[0]):
                assert (
                    content["markups"][0]["controlPoints"][idx]["position"]
                ) == (
                    [
                        str(afids_coords[idx][0]),
                        str(afids_coords[idx][1]),
                        str(afids_coords[idx][2]),
                    ]
                )

        # Delete created file
        remove(out_json_fpath)


class TestAfidsIOGeneral:
    @given(afids_coords=afid_coords(bad_range=True))
    def test_invalid_num_afids(self, afids_coords: NDArray[np.single]) -> None:
        with tempfile.NamedTemporaryFile(
            mode="w", prefix="sub-test_desc-", suffix="_afids.fcsv"
        ) as out_fcsv_file:
            with pytest.raises(TypeError) as err:
                afids_to_fcsv(afids_coords, out_fcsv_file)

            assert "AFIDs, but received" in str(err.value)

    @given(afids_coords=afid_coords(bad_dims=True))
    def test_invalid_afids_dims(
        self, afids_coords: NDArray[np.single]
    ) -> None:
        with tempfile.NamedTemporaryFile(
            mode="w", prefix="sub-test_desc-", suffix="_afids.fcsv"
        ) as out_fcsv_file:
            with pytest.raises(TypeError) as err:
                afids_to_fcsv(afids_coords, out_fcsv_file)

            assert "Expected 3 spatial dimensions" in str(err.value)
