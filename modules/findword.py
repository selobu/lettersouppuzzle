# coding: utf-8

from .readData import CrosswordData
from collections import namedtuple
from .errors import ErrorCode
from typing import List

Point = namedtuple("Point", ["row", "col"])
Position = namedtuple("Positions", ["initpoint", "endpoint"])


def __validateword__(word: str, maxsize=10):
    """check if all characters are valid, if not then raise a error

    Args:
        word: Array of valid characters
              - minimum word size 3
    """
    if len(word) < 3:
        raise ErrorCode(408, message=f"len(word) == {len(word)}")
    if len(word) > maxsize:
        raise ErrorCode(409, message=f"len(word) == {len(word)}")
    not_allowed = [character for character in word if not(65 <= ord(character) <= 90)]
    if len(not_allowed) > 0:
        not_allowed = ", ".join([str(i) for i in not_allowed])
        raise ErrorCode(404, "Word has not allowed characters:[{not_allowed}]")


def __searchword(word, col: int, rawdata: list) -> list:
    """searching positions in the rawdata

    Args:
        word (_type_): word to be searched
        col (int): place to split the array and check
        rawdata (_type_): list of characters to be found

    Return:
        list: positions where the word were found
    """
    wordlen = len(word)
    if wordlen > len(rawdata):
        return []
    left = rawdata[:col]
    left.append(word[0])
    rigth = rawdata[col:]
    left = left[::-1]
    left = "".join(left)
    rigth = "".join(rigth)
    res = []
    if len(left) >= wordlen:
        if word in left:
            res.append((len(left) - wordlen, col))
            
    if len(rigth) >= wordlen:
        if word in rigth:
            res.append((col, col + len(word)-1))
    return res


def findWord(word: str, matrix: CrosswordData) -> List[Position]:
    """find word position of a given matrix

    Args:
        word (str): word to be searched
        matrix (CrosswordData): character matrix

    Returns:
        list: list of Positions, empty list if not found.

    each position contains two points wich correspond to init and end point positions.
    """
    data = matrix
    __validateword__(word, maxsize=len(data))

    # getting word's first character
    firstchar = word[0]
    # find word positions
    points = list()
    for rownumber, row in enumerate(matrix):
        for colnumner, char in enumerate(row):
            if char == firstchar:
                points.append(Point(rownumber, colnumner))

    # for each point
    # 1-search horz word
    for point in points:
        row = point.row
        col = point.col
        rowdata = matrix[row]
        wordPositions = __searchword(word, col, rowdata)
        rows = [Position(Point(row, p[0]), Point(row,p[1])) for p in wordPositions]
        
    # 1-search vert word
   
    
    print(rows)
