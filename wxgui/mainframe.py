import wx
from configuration import config
import wx.lib.agw.xlsgrid as XG
import wx.grid as gridlib


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
        self.create_ui()
        self.CreateMenuAndStatusBar()
        self.CenterOnScreen()
        self.Layout()

    def create_ui(self):
        panel = XLSGridPanel(self)

    def CreateMenuAndStatusBar(self):
        pass


class SimpleGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)
        self.moveTo = None
        self.create()

    def create(self, nrows=25, ncols=25):
        self.CreateGrid(nrows, ncols)

    def setmatrixdata(self, matrix):
        for rownumber, row in enumerate(matrix):
            for colnumber, element in row:
                self.SetCellValue(rownumber, colnumber, str(element))


class XLSGridPanel(wx.Panel):
    def __init__(self, parent):

        wx.Panel.__init__(self, parent)

        self.grid = SimpleGrid(self)

        self.grid.Hide()

        self.DoLayout()

    def DoLayout(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        top_center_sizer = wx.BoxSizer(wx.VERTICAL)
        top_center_sizer.Add((0, 0), 1, wx.EXPAND, 0)
        main_sizer.Add((0, 10))
        main_sizer.Add(self.grid, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(main_sizer)
        self.OnStart()

        main_sizer.Layout()

    def OnStart(self, event=None):

        busy = wx.BusyInfo("Reading contents, please wait...")

        del busy

        self.grid.Show()

        self.Layout()
