import logging
import os
from datetime import datetime

# paths for logger
base_path = '/Users/premkumar/my_pc/programming/code_git/mlops/us-visa-project/'
log_dir = os.path.join(base_path, 'logs')
log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_full_path = os.path.join(log_dir, log_file_name)

# create a folder
os.makedirs(log_dir, exist_ok=True)

# logging
logging.basicConfig(filename=logs_full_path, 
                    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
                    level=logging.DEBUG)
