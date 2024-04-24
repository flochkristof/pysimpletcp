import logging

def get_logger(level=logging.DEBUG, handler="console"):
    """Function that returns a logger object with the specified logging level and handlerű
    
    :param level: Logging level of the logger
    :type level: int
    :param handler: Handler type of the logger (console or file)
    :type handler: str
    """

    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(level)

    # Create a formatter
    formatter = logging.Formatter('[%(module)s] - %(levelname)s : %(message)s')

    # Create a console handler and set the formatter
    if handler == "console":
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
    elif handler == "file":
        file_handler = logging.FileHandler("log.txt")
        file_handler.setFormatter(formatter)
    else:
        raise ValueError("Invalid handler type")

    # Add the console handler to the logger
    logger.addHandler(console_handler)

    return logger