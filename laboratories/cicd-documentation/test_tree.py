import unittest
from tree import Tree

class TestTree(unittest.TestCase):

    def test_find_existing_node(self):
        """Test finding an existing node in the tree"""
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        tree.add(1)
        tree.add(9)
        
        node = tree.find(7)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 7)

    def test_find_non_existing_node(self):
        """Test finding a non-existing node in the tree"""
        tree = Tree()
        tree.add(5)
        tree.add(3)
        tree.add(7)
        
        node = tree.find(10)
        self.assertIsNone(node)

    def test_find_root_node(self):
        """Test finding the root node"""
        tree = Tree()
        tree.add(5)
        
        node = tree.find(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 5)

if __name__ == '__main__':
    unittest.main()