#! /usr/bin/env python3

import argparse
import csv
from datetime import datetime
import json
from pathlib import Path

MAIN_DIR = Path(__file__).parent

OUTPUT_FILE_EXTENSION = ".chat.csv"

TIMESTAMP_FROM = '%Y-%m-%dT%H:%M:%S'
TIMESTAMP_TO = '%Y-%m-%d %H:%M:%S'

CSV_HEADER_COLUMNS = "datetime", "sender", "message"


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert chat text to csv format.')
    parser.add_argument('filename', type=str, help='Path to the chat file')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    json_input_path = MAIN_DIR / args.filename
    csv_output_path = json_input_path.with_suffix(OUTPUT_FILE_EXTENSION)

    with json_input_path.open() as json_file:
        json_content = json.load(json_file)

    with csv_output_path.open("w") as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        csvwriter.writerow(CSV_HEADER_COLUMNS)
        for msg in json_content["messages"]:
            timestamp = msg.get("date") 
            formatted_timestamp = datetime.strptime(timestamp, TIMESTAMP_FROM).strftime(TIMESTAMP_TO)
            sender = msg.get("from")
            message = ''.join(entity['text'] for entity in msg['text_entities'])
            row = formatted_timestamp, sender, message
            csvwriter.writerow(row)
