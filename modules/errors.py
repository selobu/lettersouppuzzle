# coding: utf-8
import difflib # ref 
from modulesconfig import ERROR_CODES

class ErrorCode(Exception):
    def __init__(self, code):
        if code not in ERROR_CODES.keys():
            closed_error_code =  difflib.get_close_matches(code, ERROR_CODES.keys())
            raise Exception(f'Unknown error code: {code}\npossible you would like to set {closed_error_code}')
        self.code = code
    def __str__(self):
        return f'{self.code}: {ERROR_CODES[self.code]}'
