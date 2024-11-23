"""
This module defines the `Reader` class, which provides static methods 
for reading JSON data from files. The class includes functionality to 
read JSON data and convert it into Python objects.

Classes:
    Reader: A class that provides methods to read JSON files.

Usage:
    To read a JSON file, call the `read_json` method with the filename 
    as an argument. The method returns the parsed JSON data as a Python 
    object (e.g., a dictionary or list).
"""

import json
import logging

import logging_config  


logging_config.setup_logging()
logger = logging.getLogger('ReaderLogger')


class Reader:
    """
    A class for reading JSON files.

    This class provides static methods to read JSON data from files 
    and convert it into Python objects.

    Methods:
        read_json(filename: str): Reads a JSON file and returns its content.
        read_json_safe(filename: str): Attempts to read a JSON file 
                                         and handles exceptions gracefully.
    """
    @staticmethod
    def read_json(filename: str) -> None:
        """
        Reads a JSON file and returns its content.

        Args:
            filename (str): The name of the JSON file to read.

        Returns:
            dict or list: The parsed JSON data as a Python object.

        Raises:
            FileNotFoundError: If the file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            logger.info(f"Successfully read JSON data from {filename}.")
            return data
        except FileNotFoundError as e:
            logger.error(f"File not found: {filename}. Error: {e}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in file {filename}. Error: {e}")
            raise
