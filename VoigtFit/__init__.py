"""
VoigtFit is a Python package designed to fit Voigt profiles to absorption
lines in spectral data. The package handles multiple spectra simultaneously,
and fits multiple component structure of several absorption lines using a
Levenberg--Marquardt minimization algorithm to identify the optimal parameters.

Written by Jens-Kristian Krogager.
"""
from os import path
from VoigtFit import *
import dataset
import hdf5_save as hdf5
import line_complexes
import output
import regions
import voigt

__author__ = 'Jens-Kristian Krogager'

mypackage_root_dir = path.dirname(path.abspath(__file__))
with open(path.join(mypackage_root_dir, 'VERSION')) as version_file:
    __version__ = version_file.read().strip()