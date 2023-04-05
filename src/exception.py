import sys
import logging
import src.logger

def error_message_details(error, error_detail: sys):
    _, _, exc_tb = error_detail
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error present in the python script [ {0} ] line number [ {1} ] error message [ {2} ]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        self.error_message = error_message_details(error_message, error_detail=error_detail)
        super().__init__(self.error_message)

    def __str__(self):
        return self.error_message

if __name__=="__main__":
    try:
        a=1/0
    except ZeroDivisionError as e:
        error_message = "Divide by zero error"
        logging.info(error_message)
        raise CustomException(e, sys.exc_info()) 
