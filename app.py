from src.ML_PROJECT.logger import logging


from src.ML_PROJECT.exception import CustomException

import sys


if __name__ == "__main__":
    logging.info("the execution has started")
    

    try:
        a=1/0
    except Exception as e:
        logging.info("the custom exception has been raised")
        raise CustomException(e,sys)    