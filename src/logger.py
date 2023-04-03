''' sets up a logging system for your Python project. This is useful for recording information about
 what your code is doing, especially when there are errors or unexpected behavior. The 
 logging system allows you to record
 messages with different levels of severity, such as DEBUG, INFO, WARNING, ERROR, and CRITICAL.'''
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs") #getcwd means current working directory
os.makedirs(logs_path,exist_ok=True)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.INFO,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)
if __name__ == "__main__":
    logging.info("Logging has started")
