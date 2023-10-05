import logging
import os

from datetime import datetime

LOG_fILE=f"{datetime.now().strftime('%Y-%m-%d')}.log"
log_path=os.path.join(os.getcwd(),"logs",LOG_fILE)
os.makedirs(log_path, exist_ok=True)

LOG_fILE_PATH=os.path.join(log_path,LOG_fILE)

logging.basicConfig(
    filename=LOG_fILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s -%(levelname)s-%(message)s",
    level=logging.INFO,
)
