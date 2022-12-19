# codign: utf-8
from .errors import ErrorCode


class CrosswordData(object):
    """Read  the contents of the matrix

    Args:
        matriz: iterable of iterables which contains letters from A-Z
        Minimum dmensions: rows 4, columns 4"

    Return:
        None
    """

    def __init__(self, matrix: list):
        """get the matrix data and initialize it

        Args:
            matrix (list): data matrix
        """
        self._nrows = 0
        self._ncols = 0
        self._matrix = [[]]
        self.valid = False  # switch to indicate if matrix data is valid or not
        self.matrix = matrix

    def __len__(self):
        return self.nrows

    def __getitem__(self, rownumber):
        return self.matrix[rownumber]

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
        if nrows <= 4:
            raise ErrorCode(405)
        self._nrows = nrows

    @property
    def ncols(self):
        return self._ncols

    @ncols.setter
    def ncols(self, ncols):
        if ncols <= 4:
            raise ErrorCode(405)
        self._cols = ncols

    def __checkifiterable__(self):
        """Check if matriz is iterable, raise a error if not"""
        if not hasattr(self.matrix, "__iter__"):
            raise ErrorCode(401)

        # checking if row elements are iterable
        for pos, row in enumerate(self.matrix):
            if not hasattr(row, "__iter__"):
                raise ErrorCode(402, message=f"row:{pos}")

    def __check_single_character__(character: str):
        """Given a character check if it's allowed, raise a error if not"""
        # converting to uppercase and check equivalent number
        number = ord(character.upper())
        if 65 <= number <= 90:
            raise ErrorCode(404, f"{character}")

    def __get_matrix_dimensions__(self) -> list:
        """Check if the matrix dimensions are consistent, , raise a error if not"""

        rows_len = [len(row) for row in self.matrix]
        rows = len(rows_len)
        if rows == 0:
            raise ErrorCode(407)
        columns = rows_len[0]

        not_consisten_rows = [
            pos for pos, i in enumerate(rows_len) if i != columns
        ]
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
