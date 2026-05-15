"""
Author: Gulraiz Khan
Filename: box.py
Description: Implementation of the Box class using MyHashMap
Date: April 3, 2026
"""

import os, sys 

sys.path.append(os.path.dirname(__file__))

from myHashMap import MyHashMap
from entry import Entry

class Box:
    def __init__(self):
        self.nicknameMap = MyHashMap()
        self.populateBox()

    """
    Adds Entries to the Box from inputFile. Assume that each
    line in inputFile corresponds to an Entry."""
    def populateBox(self, inputFile='entries.txt'):
        if not os.path.exists(inputFile):
            return

        with open(inputFile, 'r') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split()
                if len(parts) >= 2:
                    nickname = parts[0]
                    species = parts[1]
                    self.add(nickname, species)

    """
    Create an Entry object with the given information and add it
    to the nicknameMap. 
    Returns true if the Entry is successfully added to the Box, and
    false if the nickname already exists in the Box. """
    def add(self, nickname, species):
        if self.nicknameMap.containsKey(nickname):
            return False
            
        new_entry = Entry(nickname, species)
        return self.nicknameMap.put(nickname, new_entry)
    

    """
    Return a single Entry object with the given nickname and species.
    Should not modify the Box itself. 
    Return None if the Entry does not exist in the Box. """    
    def find(self, nickname, species):
        entry = self.nicknameMap.get(nickname)
        if entry:
            if species in str(entry):
                return entry
        return None

    """ 
    Return a list of nickanames representing all unique 
    nicknames in the Box. Should not modify the Box itself.
    Return None if the Box is empty. """
    def findAllNicknames(self):
        if self.nicknameMap.isEmpty():
            return None
        return self.nicknameMap.keys()

    """ 
    Return an Entry with the given nickname. Should not modify
    the Box itself. 
    Return None if the nickname is not in the Box. """
    def findEntryByNickname(self, nickname):
        return self.nicknameMap.get(nickname)

    """
    Remove the Entry with the given nickname from the Box. 
    Return true if successful, or false otherwise."""
    def removeByNickname(self, nickname):
        return self.nicknameMap.remove(nickname)

    """ 
    Remove the Entry with the given nickname and species. 
    Return true if successful, or false otherwise. """
    def removeEntry(self, nickname, species):
        entry = self.nicknameMap.get(nickname)
        if entry:
            if species in str(entry):
                return self.nicknameMap.remove(nickname)
        return False

if __name__ == '__main__':
    my_box = Box()
    print("Manual Test Results:")
    print(f"Adding 'Zelda' (Fox): {my_box.add('Zelda', 'Fox')}")
    sparky = my_box.find('Sparky', 'Pikachu')
    print(f"Find Sparky (Pikachu): {sparky}")