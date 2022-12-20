import pytest
from modules.readData import CrosswordData
from modules.findword import findWord

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


def test_search1():
    word2search = "USG"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=1, col=2), endpoint=Point(row=3, col=4))]'

def test_search2():
    word2search = "GSU"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=1, col=2), endpoint=Point(row=3, col=4))]'

def test_search3():
    word2search = "RAGO"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=1, col=1), endpoint=Point(row=4, col=4))]'

def test_search4():
    word2search = "OGAR"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=1, col=1), endpoint=Point(row=4, col=4))]'
    
def test_search5():
    word2search = "CASA"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=2, col=1), endpoint=Point(row=2, col=4))]'

def test_search6():
    word2search = "ASAC"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=2, col=1), endpoint=Point(row=2, col=4))]'

def test_search7():
    word2search = "EHOJ"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=5, col=3), endpoint=Point(row=2, col=6))]'

def test_search8():
    word2search = "JOHE"
    founded = findWord(word2search, data)
    assert str(founded) == '[Positions(initpoint=Point(row=5, col=3), endpoint=Point(row=2, col=6))]'
