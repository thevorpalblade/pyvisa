# -*- coding: utf-8 -*-
"""
    pyvisa
    ~~~~~~

    Python wrapper of National Instrument (NI) Virtual Instruments Software
    Architecture library (VISA).

    This file is part of PyVISA.

    :copyright: (c) 2014 by the PyVISA authors.
    :license: MIT, see COPYING for more details.
"""



import os
import sys
import pkg_resources
import subprocess
import configparser
from . import vpp43

__version__ = "unknown"
try:  # try to grab the commit version of our package
    __version__ = (subprocess.check_output(["git", "describe"],
                                           stderr=subprocess.STDOUT,
                                           cwd=os.path.dirname(os.path.abspath(__file__)))).strip()
except:  # on any error just try to grab the version that is installed on the system
    try:
        __version__ = pkg_resources.get_distribution('pint').version
    except:
        pass  # we seem to have a local copy without any repository control or installed without setuptools
              # so the reported version will be __unknown__

_config_parser = configparser.ConfigParser()
_config_parser.read([os.path.join(sys.prefix, "share", "pyvisa", ".pyvisarc"),
                     os.path.join(os.path.expanduser("~"), ".pyvisarc")])
try:
    _visa_library_path = _config_parser.get("Paths", "visa library")
except configparser.Error:
    pass
else:
    vpp43.visa_library.load_library(_visa_library_path)
