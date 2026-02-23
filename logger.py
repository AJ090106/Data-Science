import logging

logging.basicConfig(
    filename = 'app.log',
    filemode  = 'w',
    level = logging.DEBUG,
    format= '%(asctime)s - %(name)s- %(levelname)s-%(message)s',
    datefmt = '%Y- %m-%D  %H:%M:%S'
)

logging.debug("This a debug message")
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("this is an error message")
logging.critical("this si a critical message")
