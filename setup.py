"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import sys

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

mypackage_root_dir = path.dirname(path.abspath(__file__))
with open(path.join(mypackage_root_dir, 'VoigtFit', 'VERSION')) as v_file:
    version = v_file.read().strip()

if sys.version_info[0] < 3:
    python_version_requirement = '==2.7.*'
    programming_language = 'Programming Language :: Python :: 2.7'
else:
    python_version_requirement = '>=3.5'
    v_items = version.split('.')
    v_items[0] = '3'
    version = '.'.join(v_items)
    programming_language = 'Programming Language :: Python :: 3'

setup(
    name='VoigtFit',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,

    python_requires=python_version_requirement,

    use_2to3=True,

    description='Voigt Profile Fitting in Python',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/jkrogager/VoigtFit',

    # Author details
    author='Jens-Kristian Krogager',
    author_email='krogager.jk@gmail.com',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Astronomy',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        programming_language,
    ],

    # What does your project relate to?
    keywords='voigtfit absorption analysis',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['test_data', 'docs', 'scripts', 'doc', 'VoigtFit3']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['matplotlib', 'numpy', 'scipy',
                      'lmfit', 'h5py', 'astropy', 'numba'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'VoigtFit/static': ['Asplund2009.dat',
                            'linelist.dat',
                            'C_complexes.dict.pickle',
                            'C_full_labels.txt',
                            'telluric_em_abs.npz',
                            'input_template.txt'],
        'VoigtFit': ['VERSION'],
    },

    include_package_data=True,

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    data_files=[],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'VoigtFit=VoigtFit:main',
        ],
    },
)
