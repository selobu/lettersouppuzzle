# codign: utf-8
from errors import ErrorCode
def __checkdimensions__(matrix:list)->bool:
    """Check if the matrix dimensions are consistent
    
    Return:
        Boolean: True if the dimensions are right
    """
    if not hasattr(matrix, '__iter__'):
        raise ErrorCode(401)
    
    

def readData(matrix:list)->None:
    """Read  the contents of the matrix and stores as a global variable
    
    Parameters:
        matriz: iterable of iterables which contains letters from A-Z 
    
    Return:
        None
    """
    pass