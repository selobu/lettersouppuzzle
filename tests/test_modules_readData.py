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

def test_not_iterable_row():
    matrix= [1,['a','b','c']]
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '402'
    
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
    assert e.code == '405'

def test_small_matrix():
    matrix= [['A','B','C'],['C','D','E'],['F','G','H']]
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '405'
    
def test_matrix_missing_column():
    matrix= [['A','B','C','D'],['C','D','E','F'],['F','G','H'], ['F','G','H','U']]
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '403'
    
def test_matrix_not_allowed_character():
    matrix= [['A','B','C','D'],['C','D','E','F'],['F','G','H','ñ'], ['F','G','H','ñ']]
    try:
        CrosswordData(matrix)
    except Exception as exc:
        e = exc    
    
    assert e.__class__ == ErrorCode
    assert e.code == '404'