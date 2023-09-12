import unittest
from main import *

tree = Tree()
node_names = []
parent_names = []

class TestTreeAPI(unittest.TestCase):
    def setUp(self):
        global tree
        global node_names
        global parent_names
        node_names , parent_names = read_csv_and_preprocess("data/input1.csv")
        #self.node_names = ["A", "B", "C", "D", "E", "F"]
        #self.parent_names = [None, "A", "A", "B", "B", "C"]
        tree.buildTree(node_names, parent_names)

    def test_get_parent(self):
        global tree
        global node_names
        global parent_names
        self.assertEqual(tree.get_parent("B"), "A")
        self.assertEqual(tree.get_parent("F"), "C")
        self.assertEqual(tree.get_parent("C"), "A")
        self.assertEqual(tree.get_parent("E"), "B")
        self.assertEqual(tree.get_parent("P"), "I")
        self.assertEqual(tree.get_parent("Q"), "J")
        self.assertEqual(tree.get_parent("J"), "E")
        self.assertEqual(tree.get_parent("K"), "F")


    def test_get_children(self):
        global tree
        self.assertEqual(tree.get_children("A"), ["B", "C"])
        self.assertEqual(tree.get_children("B"), ["D", "E"])
        self.assertEqual(tree.get_children("C"), ["F","G"])
        self.assertEqual(tree.get_children("K"), ["S"])
        self.assertEqual(tree.get_children("Q"), [])
        self.assertEqual(tree.get_children("H"), ["N","O"])


    def test_get_peers(self):

        global tree
        self.assertEqual(tree.get_peers("K"), [])
        self.assertEqual(tree.get_peers("J"), [])
        self.assertEqual(tree.get_peers("T"), [])
        self.assertEqual(tree.get_peers("R"), ["Q"])
        self.assertEqual(tree.get_peers("N"), ["O"])



    def test_get_tree_till_parent(self):
        global tree
        self.assertEqual(tree.get_tree_till_parent("D"), ["A", "B", "D"])
        self.assertEqual(tree.get_tree_till_parent("A"), ["A"])
        self.assertEqual(tree.get_tree_till_parent("K"), ["A", "C", "F","K"])


if __name__ == '__main__':
    unittest.main()
