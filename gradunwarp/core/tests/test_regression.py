import numpy as np
from numpy.testing import assert_equal, assert_array_equal, \
    assert_array_almost_equal, assert_almost_equal

from gradunwarp.core import coeffs, utils
from gradunwarp.core.unwarp_resample import siemens_B

def test_siemens_B():
    gradfile = 'gradunwarp/core/tests/data/gradunwarp_coeffs.grad'
    siemens_coeffs = coeffs.get_coefficients('siemens', gradfile)
    R0 = siemens_coeffs.R0_m  * 1000

    vec = np.linspace(-300, 300, 60, dtype=np.float32)
    x, y ,z = utils.meshgrid(vec, vec, vec)

    bx = siemens_B(siemens_coeffs.alpha_x, siemens_coeffs.beta_x, x, y, z, R0)
    ref_bx = np.load('gradunwarp/core/tests/data/siemens_B_output.npz')['bx']

    # changes in legendre function is causing differences at 6th decimal
    assert_array_almost_equal(ref_bx, bx, decimal=5)
