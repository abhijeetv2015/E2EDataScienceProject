import sys
import logging

def error_message_detail(error, error_detail: sys):
    """
    This function takes an error and error_detail as input and returns a formatted string containing the filename, line number, 
    and error message. It is used to provide detailed information about exceptions that occur during program execution.
    """
    _,_,exec_tb = error_detail.exc_info()
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        exec_tb.tb_frame.f_code.co_filename,
        exec_tb.tb_lineno,
        str(error)
    )
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        """
        Initializes the CustomException with an error message and error detail.
        
        Parameters:
        - error_message: The error message to be associated with the exception.
        - error_detail: The sys module, used to extract detailed information about the exception.
        """
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the string representation of the CustomException, which is the detailed error message.
        """
        return self.error_message