import csv
import json
import jsonschema
from tree import Tree
import argparse
INPUT_SCHEMA_PATH = 'schemas/input_schema.json'
OUTPUT_SCHEMA_PATH = 'schemas/output_schema.json'
output_json_file = 'data/output.json'
with open(INPUT_SCHEMA_PATH, 'r') as input_schema_file:
    input_schema = json.load(input_schema_file)

with open(OUTPUT_SCHEMA_PATH, 'r') as output_schema_file:
    output_schema = json.load(output_schema_file)

def read_csv_and_preprocess(csv_file):
    node_names = []
    parent_names = []
    treeObj = Tree()
    if validate_input_data(csv_file,input_schema):

        try:
            with open(csv_file, 'r') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    node_name = row.get('Node', '').strip()
                    parent_name = row.get('Parent', '').strip()

                    if node_name:
                        node_names.append(node_name)
                    if parent_name:
                        parent_names.append(parent_name)
            treeObj.buildTree(node_names,parent_names)
            create_tree_structure(node_names,parent_names)
            generate_json_output(treeObj,output_json_file)
            if validate_output_data(output_json_file,output_schema):
                return treeObj ,node_names, parent_names
            else: return None , None , None

        except FileNotFoundError:
            print(f"Error: The CSV file '{csv_file}' not found.")
            return None,None, None
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {e}")
            return None,None, None
    else : return None ,None, None
    





def validate_input_data(input_csv_file, input_schema):
    try:
        with open(input_csv_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
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



def generate_json_output(tree, output_json_file):
    tree_structure = {}

    tree_structure = tree.get_tree_till_all_leaves(tree.root.name)
    tree_structure = {key: value for key, value in sorted(tree_structure.items())}
    with open(output_json_file, 'w') as file:
        json.dump(tree_structure, file, indent=4)


def main():
    parser = argparse.ArgumentParser(description="Process CSV data and generate a tree structure.")

    # Add command-line options for input and output file paths
    parser.add_argument("--input", required=False, help="Path to the input CSV file")
    parser.add_argument("--output", required=False, help="Path to the output JSON file")

    # Parse command-line arguments
    args = parser.parse_args()

    # Use the specified input and output file paths
    input_csv_file = args.input
    output_json_file = args.output

    if input_csv_file is None:
        input_csv_file = "data/input1.csv"

    if output_json_file is None:
        output_json_file = "data/output.json"


    node_names, parent_names = read_csv_and_preprocess(input_csv_file)

    if node_names and parent_names:
        # Create and build the tree
        tree = Tree()
        tree.buildTree(node_names, parent_names)

        # Validate input data
        if validate_input_data(input_csv_file, input_schema):
            # Generate JSON output
            generate_json_output(tree, output_json_file)
            create_tree_structure(node_names,parent_names)
            # Validate output data
            if validate_output_data(output_json_file, output_schema):
                print("Processing completed successfully.")

def create_tree_structure(node_names, parent_names):
    # Create a dictionary to store node references by name
    node_dict = {}

    # Create the root node (assuming the first node is the root)
    root_name = node_names[0]
    root_node = {"name": root_name, "children": []}
    node_dict[root_name] = root_node

    # Iterate through nodes and parent relationships to build the tree
    for i in range(1, len(node_names)):
        node_name = node_names[i]
        parent_name = parent_names[i]

        # Create a new node
        new_node = {"name": node_name, "children": []}
        node_dict[node_name] = new_node

        # Attach the new node to its parent
        parent_node = node_dict[parent_name]
        parent_node["children"].append(new_node)

    with open("data/frontStructure.json", 'w') as file:
        json.dump(root_node, file, indent=4)

    return root_node

#if __name__ == "__main__":
    #main()
if __name__ == "__main__":
    input_csv_file = 'data/input.csv'
    output_json_file = 'data/output.json'
    #nodes =      ["A","B","C","D","E","F","G","H","I"]
    treeObj ,nodes , parents = read_csv_and_preprocess(input_csv_file)
    print(nodes)
    print(parents)
    #parents = ["null","A","A","B","B","C","F","E","E"]
    #visualize_tree(treeObj.root)
    print(treeObj.get_tree_till_parent("C"))
    #create_tree_structure(nodes,parents)