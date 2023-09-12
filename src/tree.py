import json
class treeNode:

    def __init__(self,name,parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def appendChildNode(self,child):
        self.children.append(child)
    

class Tree:

    def __init__(self):
        self.nodes = {}
        self.root = None

    def createNode(self,name,parent):
        node = treeNode(name = name , parent= parent)
        self.nodes[name] = node

        if parent == "null": self.root = node
        return node
    
    def buildTree(self, nodes, parents):
        for node_name, parent_name in zip(nodes, parents):
            node = self.nodes.get(node_name) or self.createNode(node_name, parent_name)
            if parent_name != 'null':
                parent = self.nodes.get(parent_name) or self.createNode(parent_name, None)
                parent.appendChildNode(node)

    def get_parent(self, node_name):
        node = self.nodes.get(node_name)
        if node:
            parent = node.parent
            return parent if parent else None
        return None

    def get_children(self, node_name):
        node = self.nodes.get(node_name)
        if node:
            return [child.name for child in node.children]
        return []

    def get_peers(self, node_name):
        node = self.nodes.get(node_name)
        if node and node.parent:
            parentNode = self.nodes.get(node.parent)
            return list(set([child.name for child in parentNode.children if child != node]))
        
        return []

    def get_tree_till_parent(self, node_name):
        node = self.nodes.get(node_name)
        path = []
        while node:
            path.insert(0, node.name)
            node = self.nodes.get(node.parent)
        return path

    def get_tree_till_all_leaves(self, node_name):
        node = self.nodes.get(node_name)
        if node:
            result = {}
            result[node_name] = {
                "children": [child.name for child in node.children],
                "parent": node.parent if node.parent else None
            }
            for child in node.children:
                result.update(self.get_tree_till_all_leaves(child.name))
            return result
        return {}

    def convert_to_subtree(self, node_name):
        node = self.nodes.get(node_name)
        if node:
            subtree = {"name": node.name, "children": []}
            for child in node.children:
                subtree["children"].append(self.convert_to_subtree(child.name))
            
            with open("data/frontStructure-test.json", 'w') as file:
               json.dump(subtree, file, indent=4)
            return subtree
        else:
            return None
    
    def inorder_traversal(self, node=None, traversal=None):
        nodes = self.nodes
        traversal = []
        for values in nodes.keys():
            traversal.append(values)
        traversal.sort()
        return traversal

    def preorder_traversal(self, node=None, traversal=None):
        if node is None:
            node = self.root

        if traversal is None:
            traversal = []

        if node:
            traversal.append(node.name)  # Current node
            for child in node.children:
                self.preorder_traversal(node=child, traversal=traversal)  # Children

        return traversal

    def postorder_traversal(self, node=None, traversal=None):
        if node is None:
            node = self.root

        if traversal is None:
            traversal = []

        if node:
            for child in node.children:
                self.postorder_traversal(node=child, traversal=traversal)  # Children
            traversal.append(node.name)  # Current node

        return traversal

    def find_depth(self, node_name, node=None, depth=0):
        if node is None:
            node = self.root

        if node:
            if node.name == node_name:
                return depth
            else:
                for child in node.children:
                    found_depth = self.find_depth(node_name, node=child, depth=depth + 1)
                    if found_depth != -1:  # Node found in the subtree
                        return found_depth

        return -1 







#treeObj = Tree()
#nodes =      ["A","B","C","D","E","F","G","H","I"]
#parents = ["null","A","A","B","B","C","F","E","E"]
#treeObj.buildTree(nodes=nodes,parents=parents)
#
#print(treeObj.get_tree_till_all_leaves("A"))
#for node_name , node  in treeObj.nodes.items():
#    print("Node :",node_name)
#    print("Parent :",node.parent)
#    print("Children :",node.children)
#    print("\n\n")