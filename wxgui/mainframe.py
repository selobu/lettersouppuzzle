import wx
from configuration import config
import wx.lib.agw.xlsgrid as XG
import wx.grid as gridlib
from random import randint
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
        self.start_button = wx.Button(self, -1, "Search")
        self.create_ui()
        self.CreateMenuAndStatusBar()
        self.CenterOnScreen()
        self.Layout()
        self.Bind(wx.EVT_BUTTON, self.onsearch, self.start_button)
        wx.CallAfter(self.populateinitdata)

    def create_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_right_sizer = wx.BoxSizer(wx.VERTICAL)
        top_center_sizer = wx.BoxSizer(wx.VERTICAL)

        top_sizer.Add(
            self.start_button,
            0,
            wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL,
            10,
        )

        self.searchword = wx.TextCtrl(self, -1, "", size=(125, -1))
        wx.CallAfter(self.searchword.SetInsertionPoint, 0)

        top_center_sizer.Add(self.searchword, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        top_sizer.Add(top_center_sizer, 0, wx.EXPAND, 0)

        label_xlrd = wx.StaticText(self, -1, "Buscar")
        top_right_sizer.Add(label_xlrd, 0, wx.ALL, 5)
        top_right_sizer.Add((0, 0), 1, wx.EXPAND, 0)

        main_sizer.Add(top_sizer, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add((0, 10))

        self.sheet = SimpleGrid(self)
        main_sizer.Add(self.sheet, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(main_sizer)

        main_sizer.Layout()

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

    def onsearch(self, evt):
        word2search = self.searchword.Value.upper()
        matrix = CrosswordData(self.sheet.data)
        result = findWord(word2search, matrix)
        self.sheet.displayresult(result)


class SimpleGrid(gridlib.Grid):
    def __init__(self, parent):
        gridlib.Grid.__init__(self, parent, -1)
        self.moveTo = None
        self.create()

    def create(self, nrows: int = 25, ncols: int = 25):
        """Create initial sheet dimensions

        Args:
            nrows (int, optional): row numbers. Defaults to 25.
            ncols (int, optional): col numbers. Defaults to 25.
        """
        self.CreateGrid(nrows, ncols)

    def displayresult(self, positions):
        for position in positions:
            points = self._linkpoints(position)
            color = randint(1, 130)
            color2 = randint(130, 255)
            color3 = randint(0, 255)
            for point in points:
                self.SetCellBackgroundColour(
                    point[0], point[1], wx.Colour(color, color2, color3)
                )
            self.Refresh()

    def _linkpoints(self, position):
        inipos = position[0]
        endpos = position[1]
        # connecting two points
        rowincrease = [[0, 1][inipos[0] < endpos[0]], -1][inipos[0] > endpos[0]]
        colincrease = [[0, 1][inipos[1] < endpos[1]], -1][inipos[1] > inipos[1]]
        res = [inipos]
        while True:
            currpoint = [res[-1][0] + rowincrease, res[-1][1] + colincrease]
            res.append(currpoint)
            if currpoint[0] == endpos[0] and currpoint[1] == endpos[1]:
                break
        return res

    @property
    def data(self) -> list:
        """grid current data

        Returns:
            list: of row contents
        """
        res = []
        for row in range(self.GetNumberRows()):
            rowdata = []
            for col in range(self.GetNumberCols()):
                rowdata.append(self.GetCellValue(row, col))
            res.append(rowdata)
        return res

    def display(self, data):
        ccols = self.GetNumberCols()
        crows = self.GetNumberRows()
        if crows > 0:
            self.DeleteRows(0, crows)
        if ccols > 0:
            self.DeleteCols(0, ccols)
        self.InsertRows(0, data.nrows)
        self.InsertCols(0, data.ncols)
        self.setmatrixdata(data)

    def setmatrixdata(self, matrix: CrosswordData):
        """loads matrix data into the sheet

        Args:
            matrix (CrosswordData): matrix content
        """
        for rownumber, row in enumerate(matrix):
            for colnumber, element in enumerate(row):
                self.SetCellValue(rownumber, colnumber, str(element))
