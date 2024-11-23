import logging


def setup_logging() -> None:
    """Sets up logging for the application.

    Sets the logging level to DEBUG and defines the message format.
    Logs are output both to the console and to the 'logging.log' file."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(),
            logging.FileHandler('logging.log')
        ]
    )