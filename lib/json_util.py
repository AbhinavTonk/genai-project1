import json
import jmespath


def read_json_string_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return str(json.load(file))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def read_json_dict_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def write_json_dict_into_file(data, file_path):
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
            print(f"Data successfully saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving data to {file_path}: {e}")


# def write_json_string_into_file(resources, file_path):
#     try:
#         with open(file_path, 'w') as file:
#             json.dump(resources, file, indent=4)
#             print(f"Data successfully saved to {file_path}")
#     except Exception as e:
#         print(f"An error occurred while saving resources to {file_path}: {e}")


def json_string_to_dict(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON string.")
        return None


def dict_to_json_string(dict):
    try:
        return json.dumps(dict, indent=4)
    except Exception as e:
        print(f"An error occurred while converting to JSON string: {e}")
        return None

def get_json_path(json_path, json_input_file):
    data = read_json_dict_from_file(json_input_file)
    try:
        return jmespath.search(json_path, data)
    except Exception as e:
        print(f"An error occurred : {e}")
        return None