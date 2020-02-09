import os
import pickle


def unpickle_all_files(directory: str, except_files=None, file_format_needed=""):
    if file_format_needed:
        file_format_needed = file_format_needed if file_format_needed[0] == "." else "." + file_format_needed
    if except_files is None:
        except_files = []
    files = {}

    try:
        list_of_files = os.listdir(directory)
    except FileNotFoundError:
        return {}

    input_directory = directory if len(directory) == 0 or directory[-1] == "/" else directory + "/"
    for file in list_of_files:
        if file not in except_files:
            if file_format_needed:
                file_format = "." + file.split(".")[-1]
                if file_format_needed != file_format:
                    continue
            with open(input_directory + file, 'rb') as f:
                files[file] = pickle.load(f)
    return files


def pickle_obj(obj, path):
    with open(path, 'wb') as handle:
        pickle.dump(obj, handle)


def unpickle_obj(path):
    with open(path, 'rb') as handle:
        return pickle.load(handle)
