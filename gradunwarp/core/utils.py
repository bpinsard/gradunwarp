### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
#
#   See COPYING file distributed along with the gradunwarp package for the
#   copyright and license terms.
#
### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ### ##
from __future__ import print_function
import numpy as np
from collections import namedtuple
import math
from math import sqrt, cos, pi


# This is a container class that has 3 np.arrays which contain
# the x, y and z coordinates respectively. For example, the output
# of a meshgrid belongs to this
# x, y, z = meshgrid(np.arange(5), np.arange(6), np.arange(7))
# cv = CoordsVector(x=x, y=y, z=z)
CoordsVector = namedtuple('CoordsVector', 'x, y, z')

from nibabel.affines import apply_affine

def transform_coordinates(A, M):
    vecs = np.asanyarray([A.x,A.y,A.z]).T
    vecs_trans = apply_affine(M, vecs)
    return CoordsVector(vecs_trans[...,0].T, vecs_trans[...,1].T, vecs_trans[...,2].T)

def get_vol_affine(infile):
    try:
        import nibabel as nib
    except ImportError:
        raise ImportError('gradunwarp needs nibabel for I/O of mgz/nifti files.'
                          ' Please install')
    nibimage = nib.load(infile)
    return np.asanyarray(nibimage.dataobj), nibimage.affine

factorial = math.factorial
