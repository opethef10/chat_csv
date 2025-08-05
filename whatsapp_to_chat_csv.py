#! /usr/bin/env python3

import argparse
import csv
from datetime import datetime
from pathlib import Path
import re

TIME_PATTERN = r'(?:0[0-9]|1[0-9]|2[0-3]):[0-5][0-9](?::[0-5][0-9])?'
SENDER_PATTERN = r'\S[^:]*?'
MESSAGE_PATTERN = r'.*?'
DATETIME_PATTERNS = (
    r'\d{4}-\d{2}-\d{2}' + " " + TIME_PATTERN,
    r'\d{2}/\d{2}/\d{4}' + ", " + TIME_PATTERN,
    r'\d{1,2}/\d{1,2}/\d{2}' + ", " + TIME_PATTERN,
)
MESSENGER_DATETIME_PATTERN = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2} [AP]M'
# ^(\d{4}-\d{2}-\d{2} \d{2}:\d{2} [AP]M)\n(?:(\S[^:]*?)\n)?(.*?)(?=\n\d{4}-\d{2}-\d{2} \d{2}:\d{2} [AP]M|\Z)

REGEX_PATTERNS = [
    re.compile(
        rf'^({datetime_pattern}) - (?:({SENDER_PATTERN}): )?({MESSAGE_PATTERN})(?=\n{datetime_pattern}|\Z)',
        re.DOTALL | re.MULTILINE
    )
    for datetime_pattern
    in DATETIME_PATTERNS
]
REGEX_PATTERNS.append(
    re.compile(
        rf'^({MESSENGER_DATETIME_PATTERN})\n(?:({SENDER_PATTERN})\n)?({MESSAGE_PATTERN})\n(?=\n{MESSENGER_DATETIME_PATTERN}|\Z)',
        re.DOTALL | re.MULTILINE
    )
)

ACCEPTED_DATETIME_FORMATS = (
    '%Y-%m-%d %H:%M:%S',
    '%d/%m/%Y, %H:%M',
    '%m/%d/%y, %H:%M',
    "%Y-%m-%d %I:%M %p"
)

TIMESTAMP_TO = '%Y-%m-%d %H:%M:%S'

MAIN_DIR = Path(__file__).parent
OUTPUT_FILE_EXTENSION = ".chat.csv"

CSV_HEADER_COLUMNS = "datetime", "sender", "message"

ERROR_MSG = (
    "Error: Whatsapp chat text file does not comply with the correct pattern!\n" +
    "Correct patterns:\n\t" +
    "\n\t".join(f"{date_format} - <sender>: <message>" for date_format in ACCEPTED_DATETIME_FORMATS)
)


def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert chat text to csv format.')
    parser.add_argument('filename', type=str, help='Path to the chat file')
    return parser.parse_args()


def convert_date(date_str, date_fmt):
    return datetime.strptime(date_str, date_fmt).strftime(TIMESTAMP_TO)


if __name__ == "__main__":
    args = parse_arguments()
    chat_path = MAIN_DIR / args.filename
    output_path = chat_path.with_suffix(OUTPUT_FILE_EXTENSION)
    text = chat_path.read_text().rstrip()

    for date_format, pattern in zip(ACCEPTED_DATETIME_FORMATS, REGEX_PATTERNS):
        all_matches = pattern.findall(text)
        if all_matches:
            all_matches = [
                (convert_date(match[0], date_format), match[1], match[2])
                for match 
                in all_matches
            ]
            break
    else:
        raise SystemExit(ERROR_MSG)

    with output_path.open("w") as csvfile:
        csvwriter = csv.writer(csvfile, lineterminator='\n')

        csvwriter.writerow(CSV_HEADER_COLUMNS)
        csvwriter.writerows(all_matches)

