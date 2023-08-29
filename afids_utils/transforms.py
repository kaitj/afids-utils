"""Methods for transforming between different coordinate systems"""
from __future__ import annotations

import numpy as np
from numpy.typing import NDArray

from afids_utils.afids import AfidPosition, AfidVoxel


def world_to_voxel(
    afid_world: AfidPosition,
    nii_affine: NDArray[np.float_],
) -> AfidVoxel:
    """
    Transform fiducials from world coordinates to voxel coordinates

    Parameters
    ----------
    afid_world
        AfidPosition containing floating-point spatial coordinates (x, y, z)
        to transform

    nii_affine
        NumPy array containing affine transformation associated with
        NifTI image

    Returns
    -------
    AfidVoxel
        Object containing transformed integer voxel coordinates (i, j, k)
    """

    # Put into numpy array for easier computation
    world_pos = np.asarray([afid_world.x, afid_world.y, afid_world.z])

    # Translation, rotation, and round to nearest voxel
    voxel_pos = world_pos.T - nii_affine[:3, 3:4]
    voxel_pos = np.dot(voxel_pos, np.linalg.inv(nii_affine[:3, :3]))
    voxel_pos = np.rint(np.diag(voxel_pos)).astype(int)

    return AfidVoxel(
        label=afid_world.label,
        i=voxel_pos[0],
        j=voxel_pos[1],
        k=voxel_pos[2],
        desc=afid_world.desc,
    )


def voxel_to_world(
    afid_voxel: AfidVoxel,
    nii_affine: NDArray[np.float_],
) -> AfidPosition:
    """
    Transform fiducials from world coordinates to voxel coordinates

    Parameters
    ----------
    afid_voxel
        AfidVoxel containing integer voxel coordinates (i, j, k)

    nii_affine
        NumPy array containing affine transformation associated with
        NifTI image

    Returns
    -------
    AfidPosition
        Object containing approximate floating-point spatial coordinates
        (x, y, z)
    """

    # Put into numpy array for easier computation
    voxel_pos = np.asarray([afid_voxel.i, afid_voxel.j, afid_voxel.k, 1])

    # Convert to float, perform rotation, translation
    world_pos = np.dot(nii_affine[:3, :3], voxel_pos)
    world_pos = world_pos + nii_affine[:3, 3:4]

    return AfidPosition(
        label=afid_voxel.label,
        x=world_pos[0],
        y=world_pos[1],
        z=world_pos[2],
        desc=afid_voxel.desc,
    )
