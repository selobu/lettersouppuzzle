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