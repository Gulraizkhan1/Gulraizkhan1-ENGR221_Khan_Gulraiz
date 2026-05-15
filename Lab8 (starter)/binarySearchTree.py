class BinarySearchTree:
    """ An implementation of an unbalanced Binary Search Tree that stores key-value pairs. """

    def __init__(self):
        self.__root = None # The root Node of this BST

    def insert(self, insertKey, insertValue):
        """ Inserts the given key and value into the BST. """
        self.__root = self.__insertHelp(self.__root, insertKey, insertValue)
    
    def __insertHelp(self, node, insertKey, insertValue):
        """ A recursive helper method to insert a new node into the BST. """
        if node == None:
            return self.__Node(insertKey, insertValue)
        elif insertKey < node.key:
            node.left = self.__insertHelp(node.left, insertKey, insertValue)
        elif insertKey > node.key:
            node.right = self.__insertHelp(node.right, insertKey, insertValue)
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
            # Case 1 & 2: One child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 3: Two children
            # Get the in-order successor (smallest in the right subtree)
            successor = self.__findSuccessorHelp(node.right)
            node.key = successor.key
            node.value = successor.value
            # Delete the successor
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
        return self.__strHelp("", self.__root)
    
    def __strHelp(self, return_string, node) -> str:
        if node == None:
            return "None"
        return "{{{}, {}, {}}}".format(node, 
                                       self.__strHelp(return_string, node.left), 
                                       self.__strHelp(return_string, node.right))

    class __Node:
        def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.value = value
            self.left = left
            self.right = right

        def __str__(self):
            return "({}, {})".format(self.key, self.value)
        
if __name__ == "__main__":
    # Quick manual check
    bst = BinarySearchTree()
    bst.insert(50, "Root")
    bst.insert(30, "Left Child")
    bst.insert(70, "Right Child")
    print("Tree structure:", bst)
    print("In-order Traversal:")
    bst.traverse()