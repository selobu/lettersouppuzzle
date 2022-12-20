import wx
from configuration import config


class MainFrame(wx.Frame):
    no_caption = [wx.DEFAULT_FRAME_STYLE, wx.NO_FULL_REPAINT_ON_RESIZE][0]

    def __init__(self, parent, title="Crossword puzzle", style=no_caption):
        # setting an appropriate size to the frame
        ca = wx.Display().GetClientArea()
        wx.Frame.__init__(
            self,
            parent,
            -1,
            title=title,
            size=wx.Size(ca[2], ca[-1]),
            pos=(ca[0], ca[1]),
            style=style,
        )

        self.Layout()
