import csv
import json




def read_csv(file_name: str) -> list:
    data = []
    with open(f'{file_name}.csv', 'r', encoding='utf-16') as file:
        reader = csv.reader(file, delimiter=';')
        for column in reader:
            data.append(column)
        data.pop(0)
    return data

def write_csv(file_name: str, data: list, headlines: list) -> None:
    """Writes data to a csv file

       Params:
        file_name(str): the name of the file being created
        data(list): the data to be written to the file
        headlines(list): table column headers    
    """
    with open(f'{file_name}.csv', 'w', newline='', encoding='utf-8') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(headlines)
        csv_writer.writerows(data)


def write_list_to_txt(file_name: str, data: list) -> None:
    """Writes data to a txt file

       Params:
        file_name(str): the name of the file being created
        data(list): the data to be written to the file
    """
    with open(f'{file_name}.txt', 'w', newline='', encoding='utf-8') as file:
        for item in data:
            file.write(f'{item}\n')


def write_json(file_name: str, data: dict) -> None:
    with open(f'{file_name}.json', 'w', encoding='utf-8') as file:        
        json.dump(data, file, indent=2)
        

def read_json(file_name: str) -> dict:
    with open(f'{file_name}.json', 'r') as file:
        data = json.load(file)
        return data