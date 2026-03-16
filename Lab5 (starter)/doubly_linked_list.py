"""
Author: Gulraiz Khan
Filename: doubly_linked_list.py
Description: Implementation of a doubly linked list
Date: March 3, 2026
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from double_node import DoubleNode 

class DoublyLinkedList():

    def __init__(self):
        self.__first_node = None
        self.__last_node = None 

    # Input: None
    # Output: A Boolean representing whether or not the list is empty
    # Description: Check whether or not the list is empty
    def is_empty(self):
        return self.get_first_node() == None
    
    # Input: None
    # Output: The first node of the list
    # Description: Get the first node of the list
    def get_first_node(self):
        return self.__first_node

    # Input: None
    # Output: The last node of the list
    # Description: Get the last node of the list
    def get_last_node(self):
        return self.__last_node

    # Input: None
    # Output: The value of the first node in the list
    # Description: Return the value of the first node in the list
    def first(self):
        if self.is_empty():
            raise Exception("Error: List is empty, cannot return first value")
        return self.get_first_node().get_value()
    
    # Input: node – the new node to set as the first node
    # Output: None
    # Description: Set the first node of the list to a new double node    
    def set_first_node(self, node):
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        else: 
            self.__first_node = node

    # Input: node – the new node to set as the last node
    # Output: None
    # Description: Set the last node of the list to a new double node
    def set_last_node(self, node):
        if node != None and type(node) != DoubleNode:
            raise Exception("Error: Input must be valid DoubleNode or None")
        else:
            self.__last_node = node

    # Input: value – the value to find
    # Output: A double node containing the value, or None
    # Description: Return a node in the list containing the given value
    def find(self, value):
        node = self.get_first_node()
        while node != None:
            if node.get_value() == value:
                return node
            node = node.get_next_node()
        return None

    # Input: value – the value to insert
    # Output: None
    # Description: Insert the given value to the front of the list
    def insert_front(self, value):
        new_node = DoubleNode(value, self.get_first_node(), None)

        if self.is_empty():
            self.set_last_node(new_node)
        else: 
            self.get_first_node().set_previous_node(new_node)

        self.set_first_node(new_node)


    # Input: value – the value to insert
    # Output: None
    # Description: Insert the given value to the back of the list
    def insert_back(self, value):
        new_node = DoubleNode(value, None, self.get_last_node())

        if self.is_empty():
            self.set_first_node(new_node)
        else:
            self.get_last_node().set_next_node(new_node)

        self.set_last_node(new_node)

    # Input: value_to_add, after_value
    # Output: A Boolean representing if the insertion was successful
    # Description: Insert a value into the list after a specified value
    def insert_after(self, value_to_add, after_value):
        node = self.find(after_value)
        if node == None:
            return False
        
        if node == self.get_last_node():
            self.insert_back(value_to_add)
        else: 
            new_node = DoubleNode(value_to_add, node.get_next_node(), node)
            node.get_next_node().set_previous_node(new_node)
            node.set_next_node(new_node)

        return True
    
    # Input: None
    # Output: The value of the node that was deleted
    # Description: Remove the first node from the list
    def delete_first_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty")
        
        first = self.get_first_node()

        if self.get_first_node() == self.get_last_node():
            self.set_first_node(None)
            self.set_last_node(None)
        else:
            self.set_first_node(first.get_next_node())
            self.get_first_node().set_previous_node(None)
        
        return first.get_value()
       
    # Input: None
    # Output: The value of the node that was deleted
    # Description: Remove the last node from the list   
    def delete_last_node(self):
        if self.is_empty():
            raise Exception("Error: List is empty")
        
        last = self.get_last_node()

        if self.get_first_node() == self.get_last_node():
            self.set_first_node(None)
            self.set_last_node(None)
        else:
            self.set_last_node(last.get_previous_node())
            self.get_last_node().set_next_node(None)
            
        return last.get_value()
    
    # Input: value – the value to remove
    # Output: The value of the node that was deleted
    # Description: Remove a node with the specified value from the list
    def delete_value(self, value):
        if self.is_empty():
            raise Exception("Error: Cannot delete from empty list")
        
        target = self.find(value)
        if target == None:
            raise Exception("Error: Cannot find value {} in list".format(value))
        
        if target == self.get_first_node():
            return self.delete_first_node()
        elif target == self.get_last_node():
            return self.delete_last_node()
        else:
            target.get_previous_node().set_next_node(target.get_next_node())
            target.get_next_node().set_previous_node(target.get_previous_node())
            return target.get_value()

    # Input: None
    # Output: None
    # Description: Print each item in the list from beginning to end
    def forward_traverse(self):
        node = self.get_first_node()
        while node != None:
            print(node.get_value())
            node = node.get_next_node()
        
    # Input: None
    # Output: None
    # Description: Print each item in the list in reverse order
    def reverse_traverse(self):
        node = self.get_last_node()
        while node != None:
            print(node.get_value())
            node = node.get_previous_node()

    # Input: None
    # Output: The number of nodes in the list
    # Description: Overloads the built-in len() method
    def __len__(self):
        l = 0
        node = self.get_first_node() 
        while node != None:
            l += 1
            node = node.get_next_node()
        return l
    
    # Input: None
    # Output: A string representing the list [val1 <-> val2]
    # Description: Overloads the built-in str() method
    def __str__(self):
        out = "["
        node = self.get_first_node() 
        while node != None:
            if len(out) > 1:
                out += " <-> "
            out += str(node)
            node = node.get_next_node()
        return out + "]"
    
if __name__ == "__main__":
    pass
