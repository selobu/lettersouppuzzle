import wx
from configuration import config
import wx.lib.agw.xlsgrid as XG
import wx.grid as gridlib

from modules.readData import CrosswordData
from modules.findword import findWord

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
        wx.CallAfter(self.populateinitdata)

    def create_ui(self):
        self.sheet = SimpleGrid(self)

    def CreateMenuAndStatusBar(self):
        pass
    
    def populateinitdata(self, *args):
        matrix = [
            "DEYQAUG",
            "XRGTUAV",
            "SCASABE",
            "XAJGUHV",
            "FMOROLB",
            "gAHJENE",
        ]
        matrix = [[u for u in s.upper()] for s in matrix]
        data = CrosswordData(matrix)
        self.sheet.display(data)


class SimpleGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)
        self.moveTo = None
        self.create()

    def create(self, nrows=25, ncols=25):
        self.CreateGrid(nrows, ncols)
        
    def display(self, data):
        ccols = self.GetNumberCols()
        crows = self.GetNumberRows()
        if crows > 0:
            self.DeleteRows(0, crows)
        if ccols > 0:
            self.DeleteCols(0, ccols)
        self.InsertRows(0,data.nrows)
        self.InsertCols(0,data.ncols)
        self.setmatrixdata(data)
        
    def setmatrixdata(self, matrix:CrosswordData):        
        for rownumber, row in enumerate(matrix):
            for colnumber, element in enumerate(row):
                self.SetCellValue(rownumber, colnumber, str(element))
