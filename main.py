# coding: utf-8
__version__ = "0.1.0"

import modules
from modules.readData import CrosswordData
from modules.findword import findWord
from pprint import pprint

if __name__ == "__main__":
    matrix = [
        "DEYQAUG",
        "XRGTUAV",
        "SCASABE",
        "XAJGUHV",
        "FMOROLB",
        "gAHJENE",
    ]
    matrix = [[u for u in s.upper()] for s in matrix]
    pprint(matrix)

    data = CrosswordData(matrix)
    data.getcol(0)
    word2search = "AUOE"
    positions = findWord(word2search, data)
