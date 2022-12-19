import pytest
from modules.readData import CrosswordData
from modules.errors import ErrorCode


def test_invalid_matriz():
    matrix= 1
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '401'
    
def test_invalid_matriz_dict():
    matrix= {}
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '407'
    
def test_empty_matriz():
    matrix= []
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '407'

def test_single_row_matrix():
    matrix= [['A','B','C']]
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '402'