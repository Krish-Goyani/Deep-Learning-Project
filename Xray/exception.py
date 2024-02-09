import os
import sys

def error_message_detail(error: Exception, error_detail:sys)->str:
    _,_, exc_tb = error_detail.exc_info()

    file_name : str=os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    error_message: str = "Error occurred python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )

    return error_message