# Log File Parser and Extractor

This Python script processes `.txt` log files from a specified folder, extracts user information, and organizes the data in a structured output file. It also renames the parsed log files by adding an `extracted_` prefix, ensuring files aren't processed multiple times.

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

### 1. Clone the repository or download the script.

```bash
git clone https://github.com/your-username/your-repo-name.git
