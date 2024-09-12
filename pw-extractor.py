import os
import argparse

def parse_log_file(file_path, setap_dict):
    setap_value = None
    user_lines = set()  # Use a set to store unique u: lines

    # Read the log file and extract relevant information
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Extract string after '#setap='
            if '#setap=' in line:
                # If we already have a setap_value, store it in the dictionary
                if setap_value and user_lines:
                    if setap_value not in setap_dict:
                        setap_dict[setap_value] = set()
                    setap_dict[setap_value].update(user_lines)
                    user_lines.clear()  # Reset for the new setap section

                setap_value = line.split('=', 1)[1].strip()

            # Extract lines that start with 'u:'
            if line.startswith('u:'):
                user_lines.add(line)

    # After reading the file, store any remaining setap_value and user_lines
    if setap_value and user_lines:
        if setap_value not in setap_dict:
            setap_dict[setap_value] = set()
        setap_dict[setap_value].update(user_lines)

def write_output_file(output_file, setap_dict):
    """Write the setap values and user lines to the output file."""
    with open(output_file, 'w') as out_file:
        for setap_value, user_lines in setap_dict.items():
            out_file.write(f"Setap Value: {setap_value}\n")
            for user_line in sorted(user_lines):  # Sort the lines for consistent output
                out_file.write(f"{user_line}\n")
            out_file.write("\n")  # Add an empty line between sections for readability

def rename_extracted_file(file_path):
    """Rename the input file by adding the prefix 'extracted_' to the filename if it doesn't already have it."""
    directory, filename = os.path.split(file_path)
    
    # Check if the file already starts with "extracted_"
    if not filename.startswith("extracted_"):
        new_filename = f"extracted_{filename}"
        new_file_path = os.path.join(directory, new_filename)
        
        os.rename(file_path, new_file_path)
        print(f"Renamed file to: {new_file_path}")
    else:
        print(f"File already prefixed with 'extracted_': {file_path}")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Parse log files and extract information.")
    parser.add_argument('-i', '--input', required=True, help="Input folder containing .txt files.")
    parser.add_argument('-o', '--output', required=True, help="Output file to store results.")

    # Parse the command-line arguments
    args = parser.parse_args()

    input_folder = args.input
    output_file = args.output

    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: Input folder '{input_folder}' does not exist.")
        return

    setap_dict = {}  # Dictionary to store setap values and their corresponding unique u: lines

    # Process all .txt files in the input folder
    for root, _, files in os.walk(input_folder):
        for file in files:
            if file.endswith('.txt'):  # Adjust to handle .txt files
                file_path = os.path.join(root, file)
                print(f"Processing file: {file_path}")
                parse_log_file(file_path, setap_dict)
                
                # After parsing, rename the file to add the 'extracted_' prefix (if not already prefixed)
                rename_extracted_file(file_path)

    # Write the final output to the output file
    write_output_file(output_file, setap_dict)

    print(f"Results written to {output_file}")

if __name__ == "__main__":
    main()
