from numpy.distutils.core import setup, Extension
from numpy.distutils.misc_util import get_numpy_include_dirs
import os, sys

mods = ['gradunwarp.core.coeffs', 'gradunwarp.core.globals',
        'gradunwarp.core.__init__', 'gradunwarp.__init__',
        'gradunwarp.core.utils',
        'gradunwarp.core.unwarp_resample',
        'gradunwarp.core.gradient_unwarp',       ]

scripts_cmd = ['gradunwarp/core/gradient_unwarp.py',]

def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration
    config = Configuration('',parent_package,top_path)
    return config

setup(name='gradunwarp',
      version = '1.3.0',
      description = 'HCP version of Gradient Unwarping Package for Python/Numpy',
      author = 'Human Connectome Project',
      py_modules  = mods,
      scripts = scripts_cmd,
      configuration=configuration,
     )
