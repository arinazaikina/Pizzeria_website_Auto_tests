import logging.config
from os import path

log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.ini')
logging.config.fileConfig(log_file_path, disable_existing_loggers=False)

pytest_plugins = [
    'src.fixtures'
]
