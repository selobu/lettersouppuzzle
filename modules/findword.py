#coding: utf-8

from .readData import CrosswordData
from collections import namedtuple



def findWord(word:str, matrix:CrosswordData )->list:
    """find word position in a given matrix

    Args:
        word (str): word to be searched
        matrix (CrosswordData): character matrix

    Returns:
        list: list of positions
    """