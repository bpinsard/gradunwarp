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


# this method is deprecated because it's slow and my suspicion that
# the matrix expressions create unnecessary temp matrices which
# are costly for huge matrices
def transform_coordinates_old(A, M):
    ''' 4x4 matrix M operates on orthogonal coordinates arrays
    A1, A2, A3 to give B1, B2, B3
    '''
    A1 = A.x
    A2 = A.y
    A3 = A.z
    B1 = A1 * M[0, 0] + A2 * M[0, 1] + A3 * M[0, 2] + M[0, 3]
    B2 = A1 * M[1, 0] + A2 * M[1, 1] + A3 * M[1, 2] + M[1, 3]
    B3 = A1 * M[2, 0] + A2 * M[2, 1] + A3 * M[2, 2] + M[2, 3]
    return CoordsVector(B1, B2, B3)

def transform_coordinates_old2(A, M):
    ''' 4x4 matrix M operates on orthogonal coordinates arrays
    A1, A2, A3 to give B1, B2, B3
    '''
    A1 = A.x
    A2 = A.y
    A3 = A.z
    A1 = A1.astype(np.float32)
    A2 = A2.astype(np.float32)
    A3 = A3.astype(np.float32)
    M = M.astype(np.float32)
    try:
        from .transform_coordinates_ext import _transform_coordinates
    except ImportError:
        raise ImportError('The transform_coordinates C extension module is missing.' \
                           ' Fallback code not yet implemented.')

    B1, B2, B3 = _transform_coordinates(A1, A2, A3, M)
    return CoordsVector(B1, B2, B3)

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


# memoized factorial
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}

    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        return self.memo[args]

factorial = math.factorial
