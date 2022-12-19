# coding: utf-8

from .readData import CrosswordData
from collections import namedtuple
from typing import List

Point = namedtuple("Point", ["row", "col"])
Positions = namedtuple("Positions", ["initpoint", "endpoint"])


def findWord(word: str, matrix: CrosswordData) -> List[Positions]:
    """find word position of a given matrix

    Args:
        word (str): word to be searched
        matrix (CrosswordData): character matrix

    Returns:
        list: list of Positions, empty list if not found.

    each position contains two points wich correspond to init and end positions.
    """
