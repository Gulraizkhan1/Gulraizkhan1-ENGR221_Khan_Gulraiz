"""
Author: Gulraiz Khan
Filename: deque.py
Description: Implementation of a double-ended queue using a doubly linked list
Date: March 3, 2026
"""

import sys, os
sys.path.append(os.path.dirname(__file__))

from doubly_linked_list import DoublyLinkedList

class Deque():
    def __init__(self):
        self.__values = DoublyLinkedList()

    # Input: None
    # Output: A Boolean representing whether or not the deque is empty
    # Description: Check whether or not the deque is empty
    def is_empty(self):
        return self.__values.is_empty()    
    
    # Input: None
    # Output: The number of items in the deque
    # Description: Overloads the built-in len() method
    def __len__(self):
        return len(self.__values) 
    
    # Input: None
    # Output: A string representing the deque
    # Description: Overloads the built-in str() method
    def __str__(self):
        return str(self.__values)
        
    # Input: None
    # Output: The value of the first item, if it exists
    # Description: Return the value of the first (leftmost) item
    def peek_left(self):
        return self.__values.first()
        
    # Input: None
    # Output: The value of the last item, if it exists
    # Description: Return the value of the last (rightmost) item
    def peek_right(self):
        if self.is_empty():
            raise Exception("Error: Deque is empty, cannot peek right")
        return self.__values.get_last_node().get_value()
        
    # Input: value – the value to insert
    # Output: None
    # Description: Insert the given value to the front (left) of the deque
    def insert_left(self, value):
        self.__values.insert_front(value)
        
    # Input: value – the value to insert
    # Output: None
    # Description: Insert the given value to the back (right) of the deque
    def insert_right(self, value):
        self.__values.insert_back(value) 
        
    # Input: None
    # Output: The value that was deleted
    # Description: Remove the first (left) item from the deque
    def remove_left(self): 
        return self.__values.delete_first_node()
        
    # Input: None
    # Output: The value that was deleted
    # Description: Remove the last (right) item from the deque
    def remove_right(self):
        return self.__values.delete_last_node()
        
if __name__ == "__main__":
    pass