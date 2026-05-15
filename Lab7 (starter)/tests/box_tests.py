import pytest
import os, sys 

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from box import Box

# add() tests 

def test_add_new_nickname():
    b = Box()
    assert b.add("UniqueName123", "Dragon") is True
    assert b.findEntryByNickname("UniqueName123") is not None

def test_add_existing_nickname():
    b = Box()
    b.add("Duplicate", "Dog")
    assert b.add("Duplicate", "Cat") is False


# find() tests 

def test_find_exists():
    b = Box()
    b.add("FoundMe", "Bird")
    result = b.find("FoundMe", "Bird")
    assert result is not None

def test_find_not_exists():
    b = Box()
    b.add("FoundMe", "Bird")
    assert b.find("FoundMe", "Fish") is None
    assert b.find("Ghost", "GhostType") is None


# findAllNicknames() tests 

def test_findAllNicknames_populated():
    b = Box()
    b.add("A", "SpeciesA")
    b.add("B", "SpeciesB")
    nicknames = b.findAllNicknames()
    assert nicknames is not None
    assert "A" in nicknames
    assert "B" in nicknames

def test_findAllNicknames_empty():
    b = Box()
    for name in b.findAllNicknames() or []:
        b.removeByNickname(name)
    assert b.findAllNicknames() is None


# findEntryByNickname() tests 

def test_findEntryByNickname_exists():
    b = Box()
    b.add("SearchKey", "Species")
    assert b.findEntryByNickname("SearchKey") is not None

def test_findEntryByNickname_not_exists():
    b = Box()
    assert b.findEntryByNickname("NonExistentKey") is None


# removeByNickname() tests 

def test_removeByNickname_exists():
    b = Box()
    b.add("DeleteMe", "Species")
    assert b.removeByNickname("DeleteMe") is True
    assert b.findEntryByNickname("DeleteMe") is None

def test_removeByNickname_not_exists():
    b = Box()
    assert b.removeByNickname("IWasNeverHere") is False


# removeEntry() tests 

def test_removeEntry_exists():
    b = Box()
    b.add("Specific", "SpeciesX")
    assert b.findEntryByNickname("Specific") is not None
    assert b.removeEntry("Specific", "SpeciesX") is True

def test_removeEntry_not_exists():
    b = Box()
    b.add("Specific", "SpeciesX")
    assert b.removeEntry("Specific", "WrongSpecies") is False
    assert b.removeEntry("Missing", "SpeciesX") is False