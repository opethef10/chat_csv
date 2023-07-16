# Chat.Csv - Chat Analyser

This script processes chat data from a CSV or GZipped CSV file and performs various analyses.

## Requirements

- Python 3.x
- Pandas library

## Installation

1. Make sure you have Python 3 installed on your system.
2. Install the required dependencies by running the following command: *(optional)*

   ```shell
   python -m pip install -r requirements.txt
   ```

This will install the necessary packages, including Pandas.

## Usage

1. Prepare your chat data in a CSV or GZipped CSV file.
2. Make sure it complies Chat.Csv structure:
   - `datetime`: The formatted timestamp of the message in `YYYY-MM-DD HH:MM:SS` format.
   - `sender`: The sender of the message.
   - `message`: The message text.
3. Open a terminal or command prompt.
4. Run the script using the following command:

   ```shell
   python __main__.py <filename>
   ```

    Replace `<filename>` with the path to your chat.csv file.

5. The script will process the chat data and generate various analyses.

   - Most Messages Sent: Shows the number of messages sent by each sender.
   - Most Characters Sent: Shows the total number of characters sent by each sender.
   - Most Sent Messages: Shows the most frequently sent messages.
   - Most Common Words: Shows the most common words used in the chat.

6. The results will be displayed in the terminal or command prompt.

## Example

Suppose you have a chat data file named "chat.csv" located in the same directory as the script.

To process the chat data and perform analyses, run the following command:

```shell
python __main__.py example.chat.csv
```

The script will display the results of the analyses based on the provided chat data.

## Notes

- The script expects the chat data to be in CSV format or GZipped CSV format. Make sure your file has the correct extension.
- The pandas library is required to run the script. If it's not already installed, follow the installation instructions provided above.
- You can process the exported Whatsapp or Telegram chat files using their respective converters in this repository.

# Whatsapp Chat to Chat.Csv Converter

This script converts a WhatsApp chat text file into CSV format.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Open a terminal or command prompt.
3. Run the script using the following command:

```shell
python whatsapp_to_chat_csv.py <filename> 
```

Replace <filename> with the path to your WhatsApp chat text file. It can be an absolute file path or file path relative to this repository directory.

The script will generate a CSV file with the same name as the input file and save it in the same directory.

## Example
Suppose you have a WhatsApp chat text file named *whatsapp_chat_with_someone.txt* located in the same directory as the script.

To convert the chat file to CSV, run the following command:

```shell
python whatsapp_to_chat_csv.py whatsapp_chat_with_someone.txt
```
A new file named *whatsapp_chat_with_someone.chat.csv* will be generated in the same directory.

## Supported Date Formats
The script supports the following date formats in the chat text file:

- YYYY-MM-DD HH:MM:SS
- DD/MM/YYYY, HH:MM

If the chat text file doesn't comply with any of these formats, an error message will be displayed.

Please make sure your chat text file follows one of the supported formats for successful conversion.

# Telegram Chat to Chat.Csv Converter

This script converts a Telegram chat JSON file into CSV format.

## Usage

1. Make sure you have Python 3 installed on your system.
2. Open a terminal or command prompt.
3. Run the script using the following command:

```shell
python telegram_json_to_chat_csv.py <filename>
```

Replace `<filename>` with the path to your Telegram chat JSON file. Default filename that Telegram exports is *result.json*

The script will generate a CSV file with the same name as the input file and save it in the same directory.

## Example

Suppose you have a Telegram chat JSON file named "chat.json" located in the same directory as the script.

To convert the chat file to CSV, run the following command:

```shell
python telegram_json_to_chat_csv.py result.json
```

A new file named *result.chat.csv* will be generated in the same directory.

## JSON Structure

The script assumes the input JSON file follows the Telegram chat JSON format. The structure should have the following key-value pairs:

- `"messages"`: An array of message objects.
- Each message object should have the following keys:
  - `"date"`: A timestamp in the format `YYYY-MM-DDTHH:MM:SS`.
  - `"from"`: The sender of the message.
  - `"text_entities"`: An array of text entity objects, where each object has a `"text"` key representing the message text.

Make sure your Telegram chat JSON file follows this structure for successful conversion.

## Output CSV Format

The generated CSV file will have the following columns:

- `datetime`: The formatted timestamp of the message in `YYYY-MM-DD HH:MM:SS` format.
- `sender`: The sender of the message.
- `message`: The message text.
