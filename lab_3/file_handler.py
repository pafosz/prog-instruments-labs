import csv
import json
import logging


"""
Module for reading and writing data to CSV, TXT, and JSON files.

Functions:
- read_csv: Reads data from a CSV file.
- write_csv: Writes data to a CSV file.
- write_json: Writes a dictionary to a JSON file.
- read_json: Reads data from a JSON file.
"""


def read_csv(file_name: str) -> list:
    """Reads data from a CSV file.

    Params:
     file_name(str): The name of the CSV file (without extension) to read data from.

    Returns:
     list: A list of rows, where each row is a list of values from the CSV file.
    """
    data = []
    try:
        with open(f"{file_name}.csv", "r", encoding="utf-16") as file:
            reader = csv.reader(file, delimiter=";")
            for column in reader:
                data.append(column)
            data.pop(0)  
        logging.info(f"Successfully read {len(data)} rows from {file_name}.csv")
    except Exception as e:
        logging.error(f"Error reading {file_name}.csv: {e}")
    return data


def write_csv(file_name: str, data: list, headlines: list) -> None:
    """Writes data to a csv file

    Params:
     file_name(str): the name of the file being created
     data(list): the data to be written to the file
     headlines(list): table column headers
    """
    try:
        with open(f"{file_name}.csv", "w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(headlines)
            csv_writer.writerows(data)
        logging.info(f"Successfully wrote {len(data)} rows to {file_name}.csv")
    except Exception as e:
        logging.error(f"Error writing to {file_name}.csv: {e}")


def read_json(file_name: str) -> dict:
    """Reads data from a JSON file.

    Params:
     file_name(str): The name of the JSON file (without extension) to read data from.

    Returns:
     dict: The data read from the JSON file, represented as a dictionary.
    """
    try:
        with open(f"{file_name}.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        logging.info(f"Successfully read data from {file_name}.json")
        return data
    except Exception as e:
        logging.error(f"Error reading {file_name}.json: {e}")
        return {}


def write_json(file_name: str, data: dict) -> None:
    """Writes a dictionary to a JSON file.

    Params:
     file_name(str): The name of the file being created (without extension).
     data(dict): The dictionary data to be written to the file.
    """
    try:
        with open(f"{file_name}.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2)
        logging.info(f"Successfully wrote data to {file_name}.json")
    except Exception as e:
        logging.error(f"Error writing to {file_name}.json: {e}")
