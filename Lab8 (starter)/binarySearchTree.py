"""
Author: Gulraiz Khan
Filename: binarySearchTree.py
Description: Implementation of a Binary Search Tree class
Date: April 13, 2026
"""

class BinarySearchTree:
    """ An implementation of an unbalanced Binary Search Tree that stores key-value pairs. """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST.
            Inputs:
                - insertKey: (any) The key to insert
                - insertValue: (any) The value to insert
            Returns: None
        """
        # Update the root to include the inserted node                
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node 
            with the given key and value into the BST.
            Inputs:
                - node: (Node) The root of the subtree to insert into
                - insertKey: (any) The key to insert
                - insertvalue: (any) The value to insert
            Returns: The node to insert """
        # Base case - Insert the node as a leaf in the appropriate location
        if node == None:
            return self.__Node(insertKey, insertValue)
        # Insert the key into the left subtree if it is less than the current key
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        # Insert the key into the right subtree if it is greater than the current key
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
        # Return the node with the node inserted
        return node

    def isEmpty(self):
        """ Returns True if the BST has no nodes, False otherwise. """
        return self.__root is None
    
    def getRoot(self):
        """ Returns the root Node of the BST. """
        return self.__root

    def search(self, goalKey):
        """ Searches for a key and returns the Node if found. """
        return self.__searchHelp(self.__root, goalKey)

    def __searchHelp(self, node, goalKey):
        """ Recursive helper to locate a specific key in the tree. """
        if node is None or node.key == goalKey:
            return node
        
        if goalKey < node.key:
            return self.__searchHelp(node.left, goalKey)
        return self.__searchHelp(node.right, goalKey)

    def lookup(self, goal):
        """ Returns the value associated with the given key. """
        node = self.search(goal)
        if node:
            return node.value
        return None

    def findSuccessor(self, subtreeRoot):
        """ Finds the node with the smallest key in a given subtree. """
        return self.__findSuccessorHelp(subtreeRoot)
    
    def __findSuccessorHelp(self, node):
        """ Smallest value is always the leftmost node. """
        if node is None or node.left is None:
            return node
        return self.__findSuccessorHelp(node.left)
    
    def delete(self, deleteKey):
        """ Deletes the node with the given key. """
        if self.search(deleteKey):
            self.__root = self.__deleteHelp(self.__root, deleteKey)
            return self.__root
        raise Exception("Key not in tree.")
    
    def __deleteHelp(self, node, deleteKey):
        """ Recursive helper to handle the three cases of BST deletion. """
        if node is None:
            return node

        if deleteKey < node.key:
            node.left = self.__deleteHelp(node.left, deleteKey)
        elif deleteKey > node.key:
            node.right = self.__deleteHelp(node.right, deleteKey)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            successor = self.__findSuccessorHelp(node.right)
            node.key = successor.key
            node.value = successor.value
            node.right = self.__deleteHelp(node.right, successor.key)

        return node

    def traverse(self) -> None:
        """ Performs an in-order traversal of the tree. """
        self.__traverseHelp(self.__root)

    def __traverseHelp(self, node) -> None:
        """ Prints the keys in ascending order. """
        if node:
            self.__traverseHelp(node.left)
            print(node)
            self.__traverseHelp(node.right)

    def __str__(self) -> str:
        """ Represent the tree as a string. Formats as 
            {(rootkey, rootval), {leftsubtree}, {rightsubtree}} """
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        """ A recursive helper method to format the tree as a string. 
            Input: 
                - return_string: (string) Accumulates the final string to output
                - node: (Node) The current node to format
            Returns: A formatted string for this node. """
        # Base case - Represent an empty branch as "None"
        if node == None:
            return "None"
        # Recursively build the string to return
        # Note, this is equivalent to
        #   return "{" + node + ", " + \
        #                self.strHelp(return_string, node.left) + ", " + \
        #                self.strHelp(return_string, node.right) + "}"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))

    ##############
    # NODE CLASS #
    ##############

    class __Node:
        """ Implementation of a node in a BST. Note that it is 
            private, so it cannot be accessed outside of a BST """

        def __init__(self, key, value, left=None, right=None):
            self.key = key         # The key of the root node of this tree
            self.value = value     # The value held by the root node of this tree
            self.left = left       # Points to the root of the left subtree
            self.right = right     # Points to the root of the right subtree

        def __str__(self):
            """ Represent the node as a string.
                Formats as "{key, value}" """
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50, "Root")
    bst.insert(30, "Left Child")
    bst.insert(70, "Right Child")
    print("Tree structure:", bst)
    print("In-order Traversal:")
    bst.traverse()