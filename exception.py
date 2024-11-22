import os, sys
from logger import logging

def error_message_detailed(error, error_detailed:sys):
    _, _, exc_tb = error_detailed.exc_info()
    
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = (
        "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
            file_name, exc_tb.tb_lineno, str(error)
        )
    )
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detailed:sys):
        super().__init__(error_message)
        self.error_message = error_message_detailed(error_message, error_detailed=error_detailed)
    
    def __str__(self):
        return self.error_message
    
    
if __name__ == "__main__":
    try:
        a = 1 / 0
        
    except Exception as e:
        logging.info("Division by Zero")
        raise CustomException(e, sys)