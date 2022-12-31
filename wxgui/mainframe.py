import wx
from configuration import config
import wx.lib.agw.xlsgrid as XG
import wx.grid as gridlib
from random import randint
from modules.readData import CrosswordData
from modules.findword import findWord


class TestSearchCtrl(wx.SearchCtrl):
    maxSearches = 5

    def __init__(
        self,
        parent,
        id=-1,
        value="",
        pos=wx.DefaultPosition,
        size=wx.DefaultSize,
        style=0,
        doSearch=None,
    ):
        style |= wx.TE_PROCESS_ENTER
        wx.SearchCtrl.__init__(self, parent, id, value, pos, size, style)
        self.Bind(wx.EVT_TEXT_ENTER, self.OnTextEntered)
        self.Bind(wx.EVT_SEARCHCTRL_SEARCH_BTN, self.OnTextEntered)
        self.Bind(wx.EVT_MENU_RANGE, self.OnMenuItem, id=1, id2=self.maxSearches)
        self.doSearch = doSearch
        self.searches = []

    def OnTextEntered(self, evt):
        text = self.GetValue()
        if self.doSearch(text):
            self.searches.append(text)
            if len(self.searches) > self.maxSearches:
                del self.searches[0]
            self.SetMenu(self.MakeMenu())
        self.SetValue("")

    def OnMenuItem(self, evt):
        text = self.searches[evt.GetId() - 1]
        self.doSearch(text)

    def MakeMenu(self):
        menu = wx.Menu()
        item = menu.Append(-1, "Recent Searches")
        item.Enable(False)
        for idx, txt in enumerate(self.searches):
            menu.Append(1 + idx, txt)
        return menu


class MainFrame(wx.Frame):
    no_caption = [wx.DEFAULT_FRAME_STYLE, wx.NO_FULL_REPAINT_ON_RESIZE][0]

    def __init__(self, parent, title="Letter soup puzzle", style=no_caption):
        # setting an appropriate size to the frame
        ca = wx.Display().GetClientArea()
        wx.Frame.__init__(
            self,
            parent,
            -1,
            title=title,
            size=wx.Size(ca[2] // 2, (ca[-1] * 2) // 3),
            pos=(ca[0], ca[1]),
            style=style,
        )
        self.create_ui()
        self.CreateMenuAndStatusBar()
        self.CenterOnScreen()
        self.Layout()

        wx.CallAfter(self.populateinitdata)

    def onreset(self, evt):
        self.populateinitdata()

    def create_ui(self):
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)

        self.sheet = SimpleGrid(self)
        main_sizer.Add(self.sheet, 1, wx.ALL | wx.EXPAND, 5)
        self.SetSizer(main_sizer)

        main_sizer.Layout()

    def CreateMenuAndStatusBar(self):
        TBFLAGS = (
            wx.TB_HORIZONTAL
            | wx.NO_BORDER
            | wx.TB_FLAT
            # | wx.TB_TEXT
            # | wx.TB_HORZ_LAYOUT
        )
        self.tb = tb = self.CreateToolBar(TBFLAGS)
        tsize = (24, 24)
        null_bmp = wx.BitmapBundle(wx.NullBitmap)
        new_bmp = wx.ArtProvider.GetBitmapBundle(wx.ART_NEW, wx.ART_TOOLBAR, tsize)
        tb.AddTool(
            10,
            "New",
            new_bmp,
            null_bmp,
            wx.ITEM_NORMAL,
            "New",
            "Reset the crossword",
            None,
        )
        self.Bind(wx.EVT_TOOL, self.OnToolClick, id=10)
        tb.AddSeparator()
        cbID = wx.NewIdRef()
        self.colsCtrl = wx.ComboBox(
            tb,
            cbID,
            "",
            choices=[str(i) for i in range(4, 50)],
            size=(50, -1),
            style=wx.CB_DROPDOWN,
        )
        tb.AddControl(self.colsCtrl)

        tb.AddStretchableSpace()
        self.search = TestSearchCtrl(tb, size=(150, -1), doSearch=self.DoSearch)
        tb.AddControl(self.search)

        self.Bind(wx.EVT_COMBOBOX, self.Onchangerows, id=cbID)
        tb.Realize()

    def OnToolClick(self, evt=None):
        self.onreset(evt)

    def Onchangerows(self, evt):
        rows = int(self.colsCtrl.Value)

    def DoSearch(self, evt):
        word2search = self.search.Value.upper()
        matrix = CrosswordData(self.sheet.data)
        result = findWord(word2search, matrix)
        self.sheet.displayresult(result)

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
        self.SetDefaultCellAlignment(wx.ALIGN_CENTRE, wx.ALIGN_CENTRE)
        self.SetDefaultColSize(50)
        self.SetDefaultRowSize(50)
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
