"""Methods for handling .json files associated with AFIDS"""
from __future__ import annotations

import json
from importlib import resources
from os import PathLike

from afids_utils.afids import AfidPosition, AfidSet
from afids_utils.exceptions import InvalidFileError


class ControlPoint:
    id: str
    label: str
    description: str
    associatedNodeID: str
    position: list[float]
    orientation: list[float]
    selected: bool
    locked: bool
    visibility: bool
    positionStatus: str


def _get_metadata(
    in_json: dict[str, bool | float | str | list[float]]
) -> tuple[str, str]:
    """Internal function to extract metadata from json files

    Note: Slicer version is not currently included in the json file

    Parameters:
    -----------
    in_json
        Data from provided json file to parse metadata from

    Returns
    -------
    parsed_version
        Slicer version associated with fiducial file

    parsed_coord
        Coordinate system of fiducials

    Raises
    ------
    InvalidFileError
        If header is invalid from .json file
    """

    # Update if future json versions include Slicer version
    parsed_version = "Unknown"
    parsed_coord = in_json["coordinateSystem"]

    # Transform coordinate system so human-understandable
    if parsed_coord == "0":
        parsed_coord = "LPS"
    elif parsed_coord == "1":
        parsed_coord = "RAS"

    if parsed_coord not in ["LPS", "RAS"]:
        raise InvalidFileError("Invalid coordinate system")

    return parsed_version, parsed_coord


def _get_afids(
    in_json: dict[str, bool | float | str | list[float]]
) -> list[AfidPosition]:
    afids = in_json["controlPoints"]

    afids_positions = []
    for afid in afids:
        afids_positions.append(
            AfidPosition(
                label=int(afid["label"]),
                x=float(afid["position"][0]),
                y=float(afid["position"][1]),
                z=float(afid["position"][2]),
                desc=afid["description"],
            )
        )

    return afids_positions


def load_json(
    json_path: PathLike[str] | str,
) -> tuple[str, str, list[AfidPosition]]:
    """Read in json and extract relevant information for an AfidSet

    Parameters
    ----------
    json_path
        Path to .json file containing AFIDs coordinates

    Returns
    -------
    slicer_version
        Slicer version associated with fiducial file

    coord_system
        Coordinate system of fiducials

    afids_positions
        List containing spatial position of afids
    """
    with open(json_path) as json_file:
        afids_json = json.load(json_file)

    # Grab metadata
    slicer_version, coord_system = _get_metadata(afids_json["markups"][0])
    # Grab afids
    afids_positions = _get_afids(afids_json["markups"][0])

    return slicer_version, coord_system, afids_positions


def save_json(
    afid_set: AfidSet,
    out_json: PathLike[str] | str,
) -> None:
    """Save fiducials to output json file

    Parameters
    ----------
    afid_set
        A complete AfidSet containing metadata and positions of AFIDs

    out_json
        Path of json file to save AFIDs to
    """
    # Read in json template
    with resources.open_text(
        "afids_utils.resources", "template.json"
    ) as template_json_file:
        template_content = json.load(template_json_file)

        # Update header
        template_content["markups"][0][
            "coordinateSystem"
        ] = afid_set.coord_system

    # Loop and update with fiducial coordinates
    for idx in range(len(template_content["markups"][0]["controlPoints"])):
        template_content["markups"][0]["controlPoints"][idx]["position"] = [
            afid_set.afids[idx].x,
            afid_set.afids[idx].y,
            afid_set.afids[idx].z,
        ]

    # Write output json
    with open(out_json, "w") as out_json_file:
        json.dump(template_content, out_json_file, indent=4)
