from sql import iterate_over_articles
import logging
from db import logging_config
logging_config()

try: 
    logging.info("starting insertion process")
    iterate_over_articles()
    logging.info("article insertion completed successfully")
except Exception as ex:
    logging.error(f"exception in main excecution {ex}")