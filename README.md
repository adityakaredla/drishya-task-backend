# drishya-task-backend

# Tree Processor

A program that reads data from a CSV file, processes the data based on predefined conditions, creates a tree structure, and exposes APIs to interact with the tree. It also writes the results to a JSON file and validates input and output data using JSON schema.

## Usage
You can run the program with the following command:
python main.py --input input_file.csv --output output_file.json

--input: Path to the input CSV file (optional, default: data/input1.csv).
--output: Path to the output JSON file (optional, default: data/output.json).

## Input CSV Format
The input CSV file should have the following format:

Node,Parent
A,null
B,A
C,A
D,B
E,B
F,C
...


