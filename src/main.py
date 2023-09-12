import csv
import json
import jsonschema
from tree import Tree
import argparse


INPUT_SCHEMA_PATH = 'schemas/input_schema.json'
OUTPUT_SCHEMA_PATH = 'schemas/output_schema.json'

with open(INPUT_SCHEMA_PATH, 'r') as input_schema_file:
    input_schema = json.load(input_schema_file)

with open(OUTPUT_SCHEMA_PATH, 'r') as output_schema_file:
    output_schema = json.load(output_schema_file)

def read_csv_and_preprocess(csv_file):
    node_names = []
    parent_names = []

    try:
        with open(csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                node_name = row.get('Node', '').strip()
                parent_name = row.get('Parent', '').strip()

                if node_name and parent_name:
                    node_names.append(node_name)
                    parent_names.append(parent_name)

        return node_names, parent_names

    except FileNotFoundError:
        print(f"Error: The CSV file '{csv_file}' not found.")
        return None, None
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return None, None





def validate_input_data(input_csv_file, input_schema):
    try:
        with open(input_csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                # Validate each row against the input schema
                jsonschema.validate(row, input_schema)

        print(f"Input CSV file '{input_csv_file}' is valid.")
        return True

    except jsonschema.exceptions.ValidationError as e:
        print(f"Input validation error: {e}")
        return False

    except Exception as e:
        print(f"An error occurred while validating input data: {e}")
        return False





def validate_output_data(output_json_file, output_schema):
    try:
        with open(output_json_file, 'r') as file:
            output_data = json.load(file)
            jsonschema.validate(output_data, output_schema)

        print(f"Output JSON file '{output_json_file}' is valid.")
        return True

    except jsonschema.exceptions.ValidationError as e:
        print(f"Output validation error: {e}")
        return False

    except Exception as e:
        print(f"An error occurred while validating output data: {e}")
        return False







def visualize_tree(node, indent=0):
    if node:
        print("  " * indent + node.name)
        for child in node.children:
            visualize_tree(child, indent + 1)


def generate_json_output(tree, output_json_file):
    tree_structure = {}

    tree_structure = tree.get_tree_till_all_leaves(tree.root.name)
    tree_structure = {key: value for key, value in sorted(tree_structure.items())}
    with open(output_json_file, 'w') as file:
        json.dump(tree_structure, file, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Process CSV data and generate a tree structure.")

    parser.add_argument("--input", required=False, help="Path to the input CSV file")
    parser.add_argument("--output", required=False, help="Path to the output JSON file")

    args = parser.parse_args()


    input_csv_file = args.input
    output_json_file = args.output

    if input_csv_file is None:
        input_csv_file = "data/input1.csv"

    if output_json_file is None:
        output_json_file = "data/output.json"


    node_names, parent_names = read_csv_and_preprocess(input_csv_file)

    if node_names and parent_names:

        tree = Tree()
        tree.buildTree(node_names, parent_names)


        if validate_input_data(input_csv_file, input_schema):

            generate_json_output(tree, output_json_file)


            if validate_output_data(output_json_file, output_schema):
                print("Processing completed successfully.")

def create_tree_structure(node_names, parent_names):
    node_dict = {}

    root_name = node_names[0]
    root_node = {"name": root_name, "children": []}
    node_dict[root_name] = root_node

    for i in range(1, len(node_names)):
        node_name = node_names[i]
        parent_name = parent_names[i]


        new_node = {"name": node_name, "children": []}
        node_dict[node_name] = new_node


        parent_node = node_dict[parent_name]
        parent_node["children"].append(new_node)

    with open("data/frontStructure.json", 'w') as file:
        json.dump(root_node, file, indent=4)
    
    return root_node


if __name__ == "__main__":
    main()
    #input_csv_file = 'data/input1.csv'
    #output_json_file = 'data/output.json'
    #treeObj = Tree()
    #nodes , parents = read_csv_and_preprocess(input_csv_file)
    #treeObj.buildTree(nodes=nodes,parents=parents)
    #generate_json_output(treeObj,output_json_file)
    #print(treeObj.get_peers("D"))