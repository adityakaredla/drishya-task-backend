from flask import Flask, jsonify , request
from main import  read_csv_and_preprocess ,validate_input_data, generate_json_output, validate_output_data ,create_tree_structure, input_schema , output_schema
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
fileNo = ""
default_csv_file = 'data/input1.csv'
input_csv_file2 = 'data/input{fileNo}.csv'
output_json_file = 'data/output.json'


tree ,node_names, parent_names = read_csv_and_preprocess(default_csv_file)

@app.route('/buildtree/<input_value>', methods=['GET'])
def get_buildtree(input_value):
    filePath = input_csv_file2.format(fileNo = input_value)
    global node_names
    global parent_names
    global tree
    tree,node_names, parent_names = read_csv_and_preprocess(filePath)
    return jsonify("Created Tree Successfully")

@app.route('/get_parent/<node_name>', methods=['GET'])
def get_parent(node_name):
    parent = tree.get_parent(node_name)
    if parent == "null" : return jsonify("No Parent Node")
    return jsonify(parent)

@app.route('/get_tree_structure', methods=['GET'])
def get_tree():
    parent = create_tree_structure(node_names,parent_names)
    return jsonify(parent)


@app.route('/get_children/<node_name>', methods=['GET'])
def get_children(node_name):
    children = tree.get_children(node_name)
    if len(children) == 0 : return jsonify("No Child Nodes Found")
    return jsonify(",".join(children))

@app.route('/get_depth/<node_name>', methods=['GET'])
def get_depth(node_name):
    children = tree.find_depth(node_name)
    if children == -1 : return jsonify("No Node Found")
    return jsonify(children)


@app.route('/get_peers/<node_name>', methods=['GET'])
def get_peers(node_name):
    peers = tree.get_peers(node_name)
    if len(peers) == 0 : return jsonify("No Peers Found")
    return jsonify(",".join(peers))

@app.route('/inorder_traversal', methods=['GET'])
def inorder_traversal():
    traversal = tree.inorder_traversal()
    return jsonify(" -> ".join(traversal))

@app.route('/preorder_traversal', methods=['GET'])
def preorder_traversal():
    traversal = tree.preorder_traversal()
    return jsonify(" -> ".join(traversal))

@app.route('/postorder_traversal', methods=['GET'])
def postorder_traversal():
    traversal = tree.postorder_traversal()
    return jsonify(" -> ".join(traversal))

@app.route('/get_tree_till_parent/<node_name>', methods=['GET'])
def get_tree_till_parent(node_name):
    path = tree.get_tree_till_parent(node_name)
    return jsonify(" -> ".join(path))

@app.route('/get_tree_till_all_leaves/<node_name>', methods=['GET'])
def get_tree_till_all_leaves(node_name):
    subtree = tree.convert_to_subtree(node_name)
    if subtree == {}: return jsonify("No Subtree Found")
    return jsonify(subtree)

if __name__ == '__main__':
    if validate_input_data(default_csv_file, input_schema):
        generate_json_output(tree, output_json_file)
        create_tree_structure(node_names,parent_names)
        if validate_output_data(output_json_file, output_schema):
            app.run(port=3010,debug=True)