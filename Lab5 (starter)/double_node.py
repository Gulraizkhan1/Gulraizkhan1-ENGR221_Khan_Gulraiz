"""
Author: Gulraiz Khan
Filename: double_node.py
Description: Implementation of a bi-directional node for a doubly linked list
Date: March 3, 2026
"""

class DoubleNode():

    def __init__(self, value, next=None, previous=None):
        self.__value = value
        self.__next_node = next
        self.__previous_node = previous 

    #####
    # Methods
    #####

    # Input: None
    # Ouput: Boolean
    # Description: Check whether or not the given node is first in the list   
    def is_first(self):
        return self.__previous_node is None
    
    # Input: None
    # Ouput: Boolean
    # Description: Check whether or not the given node is last in the list      
    def is_last(self):
        return self.__next_node is None

    #####
    # Getters
    #####

    # Input: None
    # Ouput: The value of the current double node
    # Description: Return the value of the current double node
    def get_value(self):
        return self.__value
        
    # Input: None
    # Output: The next node in the list
    # Description: Return the next node in the list
    def get_next_node(self):
        return self.__next_node
    
    # Input: None
    # Output: The previous node in the list
    # Description: Return the previous node in the list
    def get_previous_node(self):
        return self.__previous_node

    #####
    # Setters
    #####


    # Input: new_value – the new value of the node
    # Output: None
    # Description: Set the value of the node to a new value 
    def set_value(self, new_value):
        self.__value = new_value

    # Input: new_next – the new next node
    # Output: None
    # Description: Set the next node to a new node
    def set_next_node(self, new_next):
        if self.__check_valid_node(new_next):
            self.__next_node = new_next

    # Input: new_previous – the new previous node
    # Output: None
    # Description: Set the previous node to a new node
    def set_previous_node(self, new_previous):
        if self.__check_valid_node(new_previous):
            self.__previous_node = new_previous

    #####
    # Helpers
    #####

    # Input: node - the node to check
    # Output: True if valid, otherwise raises Exception
    # Description: Check whether or not the input node is of type DoubleNode or None
    def __check_valid_node(self, node):
        if type(node) != DoubleNode and node != None:
            raise Exception("Error: Input must be a valid DoubleNode or None")
        return True
    
    # Input: None
    # Output: The value of the node in string format
    # Description: Overloads the built-in __str__ method
    def __str__(self):
        return str(self.__value)

if __name__ == "__main__":
    pass