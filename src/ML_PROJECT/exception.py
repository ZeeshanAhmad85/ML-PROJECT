import sys
from src.ML_PROJECT.logger import logging


def error_message_detail(error_message,error_details:sys):
    _,_,exc_tb=error_details.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message=f"{error_message} in {file_name} at line {exc_tb.tb_lineno}"
    file_name=exc_tb.tb_lineno,str(error_message)

    return error_message



class CustomException(Exception):
    def __init__(self, error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_details)


    def __str__(self):
        return self.error_message    