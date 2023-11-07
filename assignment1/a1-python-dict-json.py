import json
import os

DICT_FILE_PATH = 'dict.json'
DEFAULT_DICT = {"apple": "omena", "pear": "päärynä", "banana": "banaani"}

def get_dictionary_data(path: str) -> dict[str, str]:
    if (os.path.isfile(path)):
        with open(path, 'r') as dict_file:
            print(dict_file)
            return json.load(dict_file)
    else:
        print("Dictionary file not found. Starting with default dictionary.")
        return DEFAULT_DICT

data_dict = get_dictionary_data(DICT_FILE_PATH)

while True:
    print("\nEnter an empty query to quit.")
    inp = input("Query: ").lower()

    if (inp == ""): break

    entry = data_dict.get(inp)

    if (entry is None):
        print(f"No translation for '{inp}'. Enter the Finnish translation to add an entry. Enter nothing to skip.")
        translation = input("Translation: ")

        if (translation != ""):
            data_dict[inp] = translation
            print("Entry added")
            continue
        else:
            print("No translation provided")
            continue
    
    print(f"{inp}: {entry}")
    
try:
    with open(DICT_FILE_PATH, 'w') as dict_file:
        json.dump(data_dict, dict_file)

except OSError as e:
    print(f"OS error occurred: {e}")

except Exception as e:
    print(f"Something went wrong when saving the dictionary. {e}")