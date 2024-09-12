# Log File Parser and Extractor

This Python script processes `.txt` log files from Flipper Zero Evilportal in a specified folder, extracts user information, and organizes the data in a structured output file. It also renames the parsed log files by adding an `extracted_` prefix, ensuring files aren't processed multiple times.

## Features

- **Setap Value Extraction**: The script extracts values following `#setap=`(wifi name) in the log files.
- **User Data Extraction**: Lines starting with `u:` are extracted, and duplicate lines within the same log file are automatically removed.
- **Organized Output**: The extracted data is grouped by `Setap Value`(wifi name) and written into a user-specified output file.
- **File Renaming**: After processing a file, it is renamed with the prefix `extracted_`.
- **Duplicate Prevention**: If a file is already prefixed with `extracted_`, it will not be renamed again.
- **Multiple File Handling**: The script processes all `.txt` files in the input folder and aggregates the results in one output file.

## Requirements

- Python 3.6+
- Works on Windows, macOS, and Linux

## Usage

### 1. Coppy Flipper Zero Evilportal Log files to your Computer
### 2. Clone the repository or download the script.

git clone https://github.com/0xSil/pw-extractor.git

### 3. Navigate to the folder where the script is located.

cd pw-extractor

### 4. Run the script with Python.

python pw-extractor.py -i <input_folder> -o <output_file>

Parameters:

    -i or --input: Specifies the folder that contains the .txt log files to be processed.
    -o or --output: Specifies the output file where the results will be stored. If this file exists, the extracted data will be appended. If theres already the AP defined, the data will be added to the AP's list.

### Example Usage

python parse_logs.py -i ./logs -o ./output/parsed_results.txt

This command processes all .txt files in the ./logs folder and writes the extracted data to ./output/parsed_results.txt.
What Happens:

    The script searches for all .txt files in the input folder.
    For each .txt file:
        It extracts values after #setap= and u: lines.
        Removes duplicate u: lines within the same log file.
        Groups the u: lines under the corresponding Setap Value.
        Renames the file by adding the extracted_ prefix, so it won't be reprocessed.
    It writes all extracted data to the output file in the following format:

Setap Value: log parsing - test
u: user1@example.com p: password1
u: user2@example.com p: password2

Setap Value: log parsing - test2
u: user3@example.com p: password3
u: user4@example.com p: password4

### Additional Notes

    Handling Duplicates: If a u: line appears multiple times in the same file, it will only be written once in the output.
    Renaming: Files that already have the prefix extracted_ will not be renamed again.
    Multiple Files: You can place multiple .txt files in the input folder, and the script will aggregate all results into one output file.

### Example Output

If two log files are processed with two different AP names, the output file might look like this:

Setap Value: log parsing - test
u: user1@test.com p: password1
u: user2@test.com p: password2

Setap Value: log parsing - test2
u: user3@test.com p: password3
u: user4@test.com p: password4

### How It Works

    Setap Value Parsing: The script looks for lines starting with #setap= in the log files and captures the value after the equal sign.
    User Data Extraction: It captures all lines starting with u:, which typically contain usernames and passwords.
    Data Aggregation: The extracted u: lines are grouped under their corresponding Setap Value, ensuring no duplicates.
    Output Writing: After all log files are processed, the results are written to the specified output file in a structured format.
    File Renaming: Once a file is processed, it is renamed with the prefix extracted_ to ensure it isn't reprocessed during future runs.

### Contributing

Feel free to contribute by opening an issue or submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.
License






