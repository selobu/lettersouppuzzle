# codign: utf-8
from .errors import ErrorCode


class CrosswordData(object):
    """Read  the contents of the matrix"""

    def __init__(self, matrix: list, allowedCharacters: list = []):
        """get the matrix data and initialize it

        Args:
            matrix (list): iterable of iterables which contains a list of single characters
                - Minimum dmensions: rows 4, columns 4"
            allowedCharacters (list): list of allowed characters, if not then only A-Z allowed
        """
        self._nrows = 0
        self._ncols = 0
        self._matrix = [[]]
        self.allowedCharacters = allowedCharacters
        self.valid = False  # switch to indicate if matrix data is valid or not
        self.matrix = matrix

    def __len__(self):
        return self.nrows

    def __getitem__(self, rownumber):
        return self.matrix[rownumber]

    def getcol(self, colnumber: int) -> list:
        """Returns data contained in the column"""
        if not (0 <= colnumber < self.ncols):
            raise ErrorCode(408)
        else:
            return [row[colnumber] for row in self.matrix]

    def getdiagonals(self, row: int, col: int) -> list:
        """getting diagonals at a given position

        Args:
            row (int): row position
            col (int): column position

        Return:
            list: list of diagonals -> [maindiagonal, reversediagonal]
        """

        if not (0 <= row <= self.nrows):
            raise ErrorCode(409)
        if not (0 <= col <= self.ncols):
            raise ErrorCode(408)
        # main diagonal search
        currcol = col
        currrow = row
        data = []
        while currcol < self.ncols and currrow < self.nrows:
            data.append(self.matrix[currrow][currcol])
            currcol += 1
            currrow += 1
        currcol = col - 1
        currrow = row - 1
        found = []
        while currcol >= 0 and currrow >= 0:
            found.append(self.matrix[currrow][currcol])
            currcol -= 1
            currrow -= 1
        # join
        found = found[::-1]
        pos2split = len(found)
        found.extend(data)
        diag1 = found, pos2split
        # end main diagonal search

        # reverse diagonal search
        currcol = col
        currrow = row
        data = []
        while currcol >= 0 and currrow < self.nrows:
            data.append(self.matrix[currrow][currcol])
            currcol -= 1
            currrow += 1
        currcol = col + 1
        currrow = row - 1
        found = []
        while currcol < self.ncols and currrow >= 0:
            found.append(self.matrix[currrow][currcol])
            currcol += 1
            currrow -= 1
        # join
        found = found[::-1]
        found.extend(data)

        diag2 = found[::-1], len(data) - 1  # left to rigth reading direction

        # end reverse diagonal search

        return diag1, diag2

    @property
    def matrix(self):
        """Return matriz data"""
        return self._matrix

    @matrix.setter
    def matrix(self, matrixdata):
        """stores the matrix data and check if the data is valid

        Args:
            matrixdata (iterable): matrix data as iterable of iterables
        """
        self._nrows = 0
        self._ncols = 0
        self.valid = False  # switch to indicate if matrix data is valid or not
        self._matrix = matrixdata
        self.__checkifiterable__()
        self.nrows, self.ncols = self.__get_matrix_dimensions__()
        for row in self.matrix:
            self.__testRowContent__(row)
        self.valid = True
        self._matrix = matrixdata

    @property
    def nrows(self):
        return self._nrows

    @nrows.setter
    def nrows(self, nrows):
        if nrows < 4:
            raise ErrorCode(405)
        self._nrows = nrows

    @property
    def ncols(self):
        return self._ncols

    @ncols.setter
    def ncols(self, ncols):
        if ncols < 4:
            raise ErrorCode(405)
        self._ncols = ncols

    def __checkifiterable__(self):
        """Check if matriz is iterable, raise a error if not"""
        if not hasattr(self.matrix, "__iter__"):
            raise ErrorCode(401)

        # checking if row elements are iterable
        for pos, row in enumerate(self.matrix):
            if not hasattr(row, "__iter__"):
                raise ErrorCode(402, message=f"row:{pos}")

    def __check_single_character__(self, character: str):
        """Given a character check if it's allowed, raise a error if not"""
        # converting to uppercase and check equivalent number
        if len(self.allowedCharacters) == 0:
            number = ord(character.upper())
            if not (65 <= number <= 90):
                raise ErrorCode(404, f"{character}")
        else:
            if character not in self.allowedCharacters:
                raise ErrorCode(404, f"{character}")

    def __get_matrix_dimensions__(self) -> list:
        """Check if the matrix dimensions are consistent, , raise a error if not"""

        rows_len = [len(row) for row in self.matrix]
        rows = len(rows_len)
        if rows == 0:
            raise ErrorCode(407)
        columns = rows_len[0]

        not_consisten_rows = [pos for pos, i in enumerate(rows_len) if i != columns]
        if len(not_consisten_rows) > 0:
            not_consisten_rows = "".join([str(i) for i in not_consisten_rows])
            raise ErrorCode(403, f"Failing rows: { not_consisten_rows }")
        return (rows, columns)

    def __testRowContent__(self, row: list) -> None:
        """Test if all row elements are considered as an english word

        Args:
            row (list): list of charactes bettween A-Z

        Returns:
            bool: True if all elements are valid else raise a error
        """
        for character in row:
            self.__check_single_character__(character)
