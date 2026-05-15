import pytest
import os, sys 


sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from myHashMap import MyHashMap

# put() tests

def test_put_empty():
    hm = MyHashMap()
    assert hm.put("key1", "val1") is True
    assert hm.get("key1") == "val1"

def test_put_nonempty_no_resize():
    hm = MyHashMap(initial_capacity=10)
    hm.put("k1", "v1")
    assert hm.put("k2", "v2") is True
    assert hm.get_size() == 2

def test_put_surpass_load_factor():
    hm = MyHashMap(initial_capacity=4, load_factor=0.75)
    hm.put("k1", "v1")
    hm.put("k2", "v2")
    hm.put("k3", "v3")
    old_cap = hm.capacity
    hm.put("k4", "v4") 
    assert hm.capacity == old_cap * 2
    assert hm.get("k1") == "v1" 

def test_put_existing_key():
    hm = MyHashMap()
    hm.put("k1", "v1")
    assert hm.put("k1", "v2") is False
    assert hm.get("k1") == "v1"

# replace() tests

def test_replace_present():
    hm = MyHashMap()
    hm.put("k1", "v1")
    assert hm.replace("k1", "new_v1") is True
    assert hm.get("k1") == "new_v1"

def test_replace_not_present():
    hm = MyHashMap()
    assert hm.replace("ghost", "value") is False

# remove() tests 

def test_remove_present():
    hm = MyHashMap()
    hm.put("k1", "v1")
    assert hm.remove("k1") is True
    assert hm.get_size() == 0
    assert hm.containsKey("k1") is False

def test_remove_not_present():
    hm = MyHashMap()
    hm.put("k1", "v1")
    assert hm.remove("k2") is False
    assert hm.get_size() == 1

# set() tests 

def test_set_present():
    hm = MyHashMap()
    hm.put("k1", "v1")
    hm.set("k1", "v2") 
    assert hm.get("k1") == "v2"
    assert hm.get_size() == 1

def test_set_not_present():
    hm = MyHashMap()
    hm.set("k1", "v1") 
    assert hm.get("k1") == "v1"
    assert hm.get_size() == 1

# get() tests 

def test_get_present():
    hm = MyHashMap()
    hm.put("color", "red")
    assert hm.get("color") == "red"

def test_get_not_present():
    hm = MyHashMap()
    assert hm.get("color") is None

# size() tests 

def test_size_empty():
    hm = MyHashMap()
    assert hm.get_size() == 0

def test_size_few():
    hm = MyHashMap()
    hm.put("k1", "v1")
    assert hm.get_size() == 1

def test_size_many():
    hm = MyHashMap()
    for i in range(100):
        hm.put(f"key{i}", i)
    assert hm.get_size() == 100

# isEmpty() tests 

def test_isEmpty_true():
    hm = MyHashMap()
    assert hm.isEmpty() is True

def test_isEmpty_false():
    hm = MyHashMap()
    hm.put("k", "v")
    assert hm.isEmpty() is False

# containsKey() tests 

def test_containsKey_exists():
    hm = MyHashMap()
    hm.put("find_me", 123)
    assert hm.containsKey("find_me") is True

def test_containsKey_not_exists():
    hm = MyHashMap()
    assert hm.containsKey("missing") is False

# keys() tests 

def test_keys_empty():
    hm = MyHashMap()
    assert hm.keys() == []

def test_keys_nonempty():
    hm = MyHashMap()
    keys_to_add = ["a", "b", "c"]
    for k in keys_to_add:
        hm.put(k, 0)
    assert set(hm.keys()) == set(keys_to_add)

# Extra: Exception Handling 

def test_none_key_exception():
    hm = MyHashMap()
    with pytest.raises(Exception):
        hm.get(None)