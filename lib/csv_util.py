#todo

import csv

def read_csv_file_as_string(file_path):
    with open(file_path, mode='r', newline='') as file:
        # reader = csv.reader(file)
        # # for row in reader:
        # #     row=row+'\n'
        # result = ' '.join(reader)
        # return reader
        return file.read()

def write_list_of_dict_into_csv_file(file_path, data):
    try:
        with open(file_path, 'w', newline='') as file:
            file.write(data)
    except Exception as e:
        print(f"An error occurred : {e}")