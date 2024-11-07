#! /usr/bin/env python

import argparse
from collections import Counter
from pathlib import Path

import pandas as pd

MAIN_FOLDER = Path(__file__).parent
FIRST_X_ROWS = 25


def parse_arguments():
    parser = argparse.ArgumentParser(description='Process chat data.')
    parser.add_argument('filename', type=str, help='Path to the chat file')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    chat_path = MAIN_FOLDER / args.filename

    if chat_path.suffix == '.gz':
        df = pd.read_csv(chat_path, compression='gzip', keep_default_na=False)
    elif chat_path.suffix == '.csv':
        df = pd.read_csv(chat_path, keep_default_na=False)
    else:
        raise ValueError("Invalid file extension. Only .csv or .gz files are accepted")

    df['characters'] = df.message.apply(len)
    df['words'] = df.message.apply(lambda x: len(x.split()))

    df2 = mostMessagesSent = df.sender.value_counts()
    df3 = mostCharactersSent = df.groupby('sender').sum('characters').sort_values('characters', ascending=False)
    df4 = mostSentMessages = df.message.value_counts()

    words = ' '.join(msg.lower() for msg in df.message.values)
    df5 = mostCommonWords = pd.DataFrame(
        Counter(words.split()).items(), columns=['word', 'frequency']
    ).sort_values(
        "frequency",
        ascending=False
    ).reset_index().drop(
        ["index"],
        axis=1
    )

    print(f"Most Messages Sent:\n{mostMessagesSent}\n")
    print(f"Most Characters Sent:\n{mostCharactersSent}\n")
    print(f"Most Sent Messages:\n{mostSentMessages.head(FIRST_X_ROWS)}\n")
    print(f"Most Common Words:\n{mostCommonWords.head(FIRST_X_ROWS)}\n")
