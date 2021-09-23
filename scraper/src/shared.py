from io import StringIO
from config import ROOT_DIR
import json
import csv
import requests


def dump_data(filename, data):
    # Dumps JSON data at configured {ROOT_DIR}

    with open(f"{ROOT_DIR}/{filename}", "w") as json_file:
        json_file.write(json.dumps(data, sort_keys=True))


def get_data(csv_url, header=False):
    # Makes a request to published sheet and
    # parses it as CSV and returns a list of rows

    response = requests.get(csv_url)
    csv_data = csv.reader(StringIO(response.text))
    csv_data = list(csv_data)
    return csv_data if header else csv_data[1:]


def clean_value(word):
    # Removes the leading whitespaces and
    # if None return empty string

    if not word:
        return ""
    return word.strip()
