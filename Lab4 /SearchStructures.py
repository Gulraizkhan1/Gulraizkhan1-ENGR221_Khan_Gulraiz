"""
Author: Gulraiz Khan
Filename: SearchStructures.py
Description: Implementation of a Stack and Queue class and their properties
Date: Feb 23, 2026
"""

# Implementation of a Stack
class Stack():
    def __init__(self):
        self.items = []

    # Input: self 
    # Output: Boolean 
    # Description: Returns True if the Stack is empty, or False if it is not empty  
    # This method checks the length of the list. If the length is 0 then it returns True meaning the Stack is empty
    def isEmpty(self):
        return len(self.items) == 0
        
    # Input: self, item
    # Output: None
    # Description: For a Stack, this should "push" item to the top of the Stack
    # This method takes a new item and adds it to the top of the Stack using the append
    def add(self, item):
        self.items.append(item)


    # Input: self
    # Output: None or the item at the top of the Stack
    # Description: For a Stack, this should "pop" an item from the Stack and return it
    # This method first calls the IsEmpty method to check if it's empty
    # If empty then it returns None
    # Otherwise, it looks at the last item at the top [-1]
    # The next line [:-1] creates a new list and includes every element except the last one at the top
    # This means it removes the last element
    # At the end the method returns the last element at the top of the Stack
    def remove(self):
        if self.isEmpty():
            return None
        
        item_at_top = self.items[-1]
        self.items = self.items[:-1]

        return item_at_top
    
# Implementation of a Queue
class Queue():
    def __init__(self):
        self.items = []

    # Input: self 
    # Output: Boolean 
    # Description: Returns True if the Queue is empty, or False if it is not empty
    # This method checks the length of the list. If the length is 0 then it returns True meaning the Queue is empty 
    def isEmpty(self):
        return len(self.items) == 0

    # Input: self, item 
    # Output: None
    # Description: For a Queue, this should "enqueue" item to the end of the Queue
    # This method takes a new item and adds it to the end of the Queue using the append
    def add(self, item):
        self.items.append(item)

    # Input: self
    # Output: None or the item at the end of the Queue
    # Description: For a Queue, this should "dequeue" an item from the Queue and return it
    # This method calls the IsEmpty method and checks to see if the Queue is empty, if empty nothing gets returned, None
    # Otherwise, we look at the first item in the Queue [0]
    # Then we create a new list and we start from the second item in the Queue all the way to the end
    # This removes the first item and shifts everything over
    # At the end of the method, it returns the first item in the Queue, which is at the front
    def remove(self):
        if self.isEmpty():
            return None
    
        item_at_front = self.items[0]
        self.items = self.items[1:]

        return item_at_front
    
    