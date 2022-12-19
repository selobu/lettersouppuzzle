# codign: utf-8
from errors import ErrorCode


def __checkifiterable__(matrix: list) -> bool:
    """Check if matriz is iterable

    Args:
        matrix: iterable of iterables which contains letters from A-Z

    Return:
        Boolean: True if all rows are iterable otherwise raise a error
    """
    if not hasattr(matrix, "__iter__"):
        raise ErrorCode(401)

    # checking if row elements are iterable
    for pos, row in enumerate(matrix):
        if not hasattr(row, "__iter__"):
            ErrorCode(402, message=f"row:{pos}")


def __get_matrix_dimensions__(matrix: list) -> list:
    """Check if the matrix dimensions are consistent
    Minimum rows 4, minimum columns 4

    Args:
        matrix: iterable of iterables which contains letters from A-Z

    Return:
        list: matrix dimensions rows x columns, otherwise raise a error
    """

    # check if matrix is iterable, if not the function automatically dispatch a error
    __checkifiterable__(matrix)

    rows_len = [len(row) for row in matrix]
    rows = len(rows_len)
    columns = rows_len[0]

    not_consisten_rows = [pos for pos, i in enumerate(rows_len) if len(i) == columns]
    if len(not_consisten_rows) > 0:
        not_consisten_rows = "".join(not_consisten_rows)
        raise ErrorCode(403, f"Failing rows: { not_consisten_rows }")
    return (rows, columns)


def __check_single_character__(character: str):
    """Given a character check if it's allowed"""
    # converting to uppercase and check equivalent number
    number = ord(character.upper())
    if 65 <= number <= 90:
        raise ErrorCode(404, f"{character}")


def __testRowContent__(row: list) -> None:
    """Test if all row elements are considered as an english word

    Args:
        row (list): list of charactes bettween A-Z

    Returns:
        bool: True if all elements are valid else raise a error
    """
    for character in row:
        __check_single_character__(character)


def readData(matrix: list) -> None:
    """Read  the contents of the matrix and stores as a global variable

    Args:
        matriz: iterable of iterables which contains letters from A-Z

    Return:
        None
    """
    pass
