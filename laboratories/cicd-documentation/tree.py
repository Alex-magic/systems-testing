from node import Node


class Tree:
    """ Tree class for binary tree """

    def __init__(self):
        """ Constructor for Tree class """
        self.root = None

    def getRoot(self):
        """ 
        Method for get root of the tree 
        
        Returns:
            Node: The root node of the tree.
        """
        return self.root

    def add(self, data):
        """ 
        Method for add data to the tree 
        
        Args:
            data (int): The value to be added to the tree.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._add(data, self.root)

    def _add(self, data, node):
        """
        Recursive helper method to add data to the tree.

        Args:
            data (int): data to add.
            node (Node): The current node being evaluated.

        Returns:
            None
        """
        if data < node.data:
            if node.left is not None:
                self._add(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right is not None:
                self._add(data, node.right)
            else:
                node.right = Node(data)

    def find(self, data):
        """
        Method for find data in the tree.

        Args:
            data (int): data to find.

        Returns:
            Node: The node containing the data, or None if not found.
        """
        if self.root is not None:
            return self._find(data, self.root)
        else:
            return None

    def _find(self, data, node):
        """
        Recursive helper method to find data in the tree.

        Args:
            data (int): data to find.
            node (Node): The current node being checked.

        Returns:
            Node: The node if found, otherwise None.
        """
        if data == node.data:
            return node
        elif (data < node.data and node.left is not None):
            return self._find(data, node.left)
        elif (data > node.data and node.right is not None):
            return self._find(data, node.right)

    def deleteTree(self):
        """
        Deletes the entire tree by setting the root to None.
        """
        self.root = None

    def printTree(self):
        """
        Prints the tree elements using Inorder traversal.
        """
        if self.root is not None:
            self._printInorderTree(self.root)

    def _printInorderTree(self, node):
        """
        Recursive helper for Inorder traversal (Left, Root, Right).

        Args:
            node (Node): The current node to start printing from.
        """
        if node is not None:
            self._printInorderTree(node.left)
            print(str(node.data) + ' ')
            self._printInorderTree(node.right)

    def _printPreorderTree(self, node):
        """
        Recursive helper for Preorder traversal (Root, Left, Right).

        Args:
            node (Node): The current node to start printing from.
        """
        if node is not None:
            print(str(node.data) + ' ')
            self._printPreorderTree(node.left)
            self._printPreorderTree(node.right)

    def _printPostorderTree(self, node):
        """
        Recursive helper for Postorder traversal (Left, Right, Root).

        Args:
            node (Node): The current node to start printing from.
        """
        if node is not None:
            self._printPostorderTree(node.left)
            self._printPostorderTree(node.right)
            print(str(node.data) + ' ')