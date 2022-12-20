#!/usr/bin/env python
# coding: utf-8
__version__ = "0.1.0"

from pprint import pprint
from os.path import dirname, abspath
import wx

import sys
import os

import myglob as sei_glob
import platform

from modules.readData import CrosswordData
from modules.findword import findWord

from wxgui.mainframe import MainFrame

_ = wx.GetTranslation
WINDOWS = platform.system() == "Windows"
LINUX = platform.system() == "Linux"
MAC = platform.system() == "Darwin"


def InitConfig():
    """Initializes the configuration data
    @postcondition: all configuration data is set

    """
    if os.path.exists(config_base):
        sei_glob.CONFIG["PROFILE_DIR"] = os.path.join(config_base, "profiles")
        sei_glob.CONFIG["PROFILE_DIR"] += os.sep
        sei_glob.CONFIG["ISLOCAL"] = True
    else:
        config_base = wx.StandardPaths.Get().GetUserDataDir()


class FocusHandler(object):
    def OnGotFocus(self, browser, **_):
        # Temporary fix for focus issues on Linux (Issue #284).
        if LINUX:
            print(
                "[wxpython.py] FocusHandler.OnGotFocus:"
                " keyboard focus fix (Issue #284)"
            )
            browser.SetFocus(True)


class MyApp(wx.App):
    def __init__(self, debug=False, *args, **kwargs):
        self.debug = debug
        wx.Log.SetLogLevel(0)
        # Disable debug popups
        wx.Log.EnableLogging(False)
        super(MyApp, self).__init__(*args, **kwargs)

        newpath = os.path.split(sys.argv[0])[0]

        paths = os.environ["PATH"].split(os.pathsep)
        if newpath not in paths:
            os.environ["PATH"] += os.pathsep + newpath
            os.environ.update()
        self.ShowMain()
        self.Bind(wx.EVT_KEY_DOWN, self.OnKeypress)

    def OnExit(self):
        return True

    def OnInit(self):
        try:
            installDir = os.path.dirname(os.path.abspath(__file__))
        except:
            installDir = os.path.dirname(os.path.abspath(sys.argv[0]))

        # decoding the path name
        self.installDir = installDir

        language = self.GetPreferences("Language")
        if not language:
            language = "Default"
        # language = "Default"
        if self.GetPreferences("LANG_DIR") is None:
            self.SetPreferences({"LANG_DIR": os.path.join(self.installDir, "locale")})
        self.locale = None
        return True

    def getDataDir(self):
        """Getting the config directory"""
        dd = wx.StandardPaths.Get()
        return dd.GetUserDataDir()

    def LoadConfig(self):
        """Checks for the option file in wx.Config."""
        userDir = self.getDataDir()
        fileName = os.path.join(userDir, "options")
        preferences = {}
        # Check for the option configuration file
        if os.path.isfile(fileName):
            options = wx.FileConfig(localFilename=fileName)
            # Check for preferences if they exist
            val = options.Read("Preferences")
            if val:
                # Evaluate preferences
                preferences = eval(val)
        return preferences

    def GetPreferences(self, preferenceKey=None, default=None):
        """
        Returns the user preferences as stored in wx.Config.
        **Parameters:**
        * 'preferenceKey': the preference to load
        * 'default': a possible default value for the preference
        """
        preferences = self.LoadConfig()
        if preferenceKey is None:
            return preferences
        optionVal = None
        if preferenceKey in preferences:
            optionVal = preferences[preferenceKey]
        else:
            if default is not None:
                preferences[preferenceKey] = default
                self.SetPreferences(preferences)
                return default
        return optionVal

    def SetPreferences(self, newPreferences):
        """
        Saves the user preferences in wx.Config.
        **Parameters:**
        * 'newPreferences': the new preferences to save
        """
        preferences = self.LoadConfig()
        config = self.GetConfig()
        for key in newPreferences:
            preferences[key] = newPreferences[key]
        config.Write("Preferences", str(preferences))
        config.Flush()

    def GetConfig(self):
        """Returns the configuration."""
        if not os.path.exists(self.GetDataDir()):
            # Create the data folder, it still doesn't exist
            os.makedirs(self.GetDataDir())
        config = wx.FileConfig(localFilename=os.path.join(self.GetDataDir(), "options"))
        return config

    def GetDataDir(self):
        """Returns the option directory for GUI2Exe."""
        sp = wx.StandardPaths.Get()
        return sp.GetUserDataDir()

    def GetVersion(self):
        return "0.1.0"

    def GetLog(self):
        """Returns the logging function used by the app
        @return: the logging function of this program instance

        """
        return self._log

    def ShowMain(self):
        self.mainFrame = MainFrame(None)
        self.mainFrame.Show(True)

    def OnKeypress(self, evt):
        key = evt.GetKeyCode()
        if key == wx.WXK_F11:
            pass
        elif key == wx.WXK_F8:
            pass
        elif key == wx.WXK_F1:
            # display the help
            pass
        else:
            evt.Skip()


if __name__ == "__main__":
    debug = True
    if platform.system() == "Linux":
        import time

        time.sleep(0.5)
    app = MyApp(debug=debug)
    app.MainLoop()
    del app


if False:
    from configuration import config
    import wx

    installDir = dirname(abspath(__file__))

    if __name__ == "__main__":
        matrix = [
            "DEYQAUG",
            "XRGTUAV",
            "SCASABE",
            "XAJGUHV",
            "FMOROLB",
            "gAHJENE",
        ]
        matrix = [[u for u in s.upper()] for s in matrix]
        pprint(matrix)

        data = CrosswordData(matrix)
        word2search = "JOHE"
        positions = findWord(word2search, data)
        print(str(positions))
