""" Adapted from GUI2Exe. """
import wx
import os


class config:
    def __init__(self, path2folder=None):
        if path2folder == None:
            userDir = wx.StandardPaths.Get().GetUserDataDir()
            self.__path = userDir
        else:
            self.__path = path2folder

    def LoadConfig(self):
        """Checks for the option file in wx.Config."""
        userDir = self.GetDataDir()
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

    def __getitem__(self, item):
        return self.GetPreferences(item)

    def __setitem__(self, item, value):
        self.SetPreferences({item: value})

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
        if self.__path == None:
            sp = wx.StandardPaths.Get()
            return sp.GetUserDataDir()
        return self.__path
