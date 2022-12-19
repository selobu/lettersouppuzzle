# coding: utf-8
__version__ = "0.1.0"

import modules
from modules.readData import CrosswordData
from pprint import pprint

if __name__ == "__main__":
    matrix = [
        ["A", "B", "C", "D"],
        ["C", "D", "E", "F"],
        ["F", "G", "H", "U"],
        ["F", "G", "H", "S"],
    ]
    pprint(matrix)
    CrosswordData(matrix)
