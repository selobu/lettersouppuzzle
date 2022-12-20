__all__ = ["SEGUNUPDATETAREAS" "VERSION", "PROG_NAME", "CONFIG"]

from configuration import config
from os.path import abspath, dirname
from os import getcwd
import sys
import wx

_ = wx.GetTranslation
pyversion = sys.version
SEGUNUPDATETAREAS = 60

HOME = getcwd()

installDir = dirname(abspath(__file__))

INSTALLDIR = installDir
CONFIG = config(path2folder=installDir)
METADATA_CREATED = False
USECHROME = False
