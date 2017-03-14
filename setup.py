#!/usr/bin/env python
import setuptools

version_string = '4.5.6a2'

setuptools.setup(
    name    = 'pyOKFrontPanel',
    license = 'MIT',
    version = version_string,
    author  = 'Qudi developers',
    author_email = 'qudi@uni-ulm.de',
    url     = 'https://github.com/Ulm-IQO/pyOKFrontPanel',
    download_url = 'https://github.com/Ulm-IQO/pyOKFrontPanel/archive/v{0}.tar.gz'.format(version_string),
    description      = 'Python CFFI wrapper for the Opal Kelly FrontPanel FPGA interface',
    keywords         = 'Opal Kelly FPGA FrontPanel',

    packages        = setuptools.find_packages(),
    setup_requires  = ["cffi>=1.0.0"],
    cffi_modules    = ["okfrontpanel/wrapper_build.py:ffibuilder"],
    install_requires= ["cffi>=1.0.0"],

    zip_safe        = False,
    package_data = {
        ''         : ['*.txt', '*.rst', '*.md'],
    },

    classifiers      = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
    ],
)

