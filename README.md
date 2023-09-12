# drishya-task-backend

# Tree Structure Using CSV and JSON

A program that reads data from a CSV file, processes the data based on predefined conditions, creates a tree structure, and exposes APIs to interact with the tree. It also writes the results to a JSON file and validates input and output data using JSON schema.

## BackEnd
- `BackEnd` folder contains the Flask App to run to facilitate the API Calls.

  ```
  python server_api.py
  ```

## Usage
The code files are present in `src`.

`schemas` contain input csv and output JSON validations.

You can run the program with the following command:

`
python main.py --input input_file.csv --output output_file.json
`

- --input: Path to the input CSV file (optional, default: data/input1.csv).

- --output: Path to the output JSON file (optional, default: data/output.json).

## Input CSV Format
The input CSV file should have the following format:
```
Node,Parent
A,null
B,A
C,A
D,B
E,B
F,C
...
```

- Each row represents a node in the tree.
- The "Node" column contains the name of the node.
- The "Parent" column contains the name of the parent node. If a node has no parent (root node), it has a "null" value in the "Parent" column.

##  Output JSON Format
The output JSON file stores the tree structure in the following format:

```
{
    "A": {
        "children": ["B", "C"],
        "parent": null
    },
    "B": {
        "children": ["D", "E"],
        "parent": "A"
    },
    "C": {
        "children": ["F"],
        "parent": "A"
    },
    ...
}
```
## Additional Features
- Error handling: The program handles cases where the input data is invalid 
- or file operations fail.
- Command-line interface (CLI): You can specify input and output file paths using command-line options.
- JSON schema validation: Input and output data are validated against JSON schemas.
- Tree traversal algorithms: In-order, pre-order, and post-order traversals are supported.
- Find the depth of a node: You can find the depth of a specific node in the tree.

## `tree.py` - Tree Class

### `Tree` Class

- `Tree` is a class that represents a tree structure.

## Methods

- `buildTree(nodes, parents)`: Builds a tree structure based on node names and their parent names.
- `get_parent(node_name)`: Returns the parent of the given node.
- `get_children(node_name)`: Returns the children of the given node.
- `get_peers(node_name)`: Returns the siblings of the given node.
- `get_tree_till_parent(node_name)`: Returns the path from the given node to its parent.
- `get_tree_till_all_leaves(node_name)`: Returns the subtree rooted at the given node, including all its descendants.
- `convert_to_subtree(node_name)`: Converts a node and its children into a specified subtree format and writes it to a JSON file.
- `inorder_traversal(node=None)`: Performs an in-order traversal of the tree and returns the list of node names.
- `preorder_traversal(node=None)`: Performs a pre-order traversal of the tree and returns the list of node names.
- `postorder_traversal(node=None)`: Performs a post-order traversal of the tree and returns the list of node names.
- `find_depth(node_name, node=None, depth=0)`: Finds the depth of a specific node in the tree.

## `main.py`
- `main.py` is the entry point of the program and contains the CLI and core functionality.
## Functions
- `read_csv_and_preprocess(csv_file)`: Reads and preprocesses the CSV file, extracting node and parent names.
- `validate_input_data(input_csv_file, input_schema)`: Validates the input CSV data against the input schema.
- `validate_output_data(output_json_file, output_schema)`: Validates the output JSON data against the output schema.
- `visualize_tree(node, indent=0)`: Visualizes the tree structure.
- `generate_json_output(tree, output_json_file)`: Generates and writes the tree structure to a JSON file.
- `create_tree_structure(node_names, parent_names)`: Creates a tree structure based on node and parent names.

