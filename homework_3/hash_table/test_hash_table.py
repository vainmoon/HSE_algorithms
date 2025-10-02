from hash_table import HashTable
import pytest


def test_set_and_get_single_item():
    hash_table = HashTable()
    hash_table["a"] = 1
    assert hash_table["a"] == 1


def test_overwrite_value():
    hash_table = HashTable()
    hash_table["a"] = 1
    hash_table["a"] = 2
    assert hash_table["a"] == 2
    assert len(hash_table) == 1


def test_len_increases_on_new_key():
    hash_table = HashTable()
    hash_table["a"] = 1
    hash_table["b"] = 2
    assert len(hash_table) == 2


def test_len_decreases_on_delete():
    hash_table = HashTable()
    hash_table["a"] = 1
    del hash_table["a"]
    assert len(hash_table) == 0


def test_delete_nonexistent_key_raises():
    hash_table = HashTable()
    with pytest.raises(KeyError):
        del hash_table["a"]


def test_get_nonexistent_key_raises():
    hash_table = HashTable()
    with pytest.raises(KeyError):
        _ = hash_table["missing"]


@pytest.mark.parametrize("key", ["string", 42, (1, 2), frozenset([1, 2])])
def test_different_hashable_keys(key):
    hash_table = HashTable()
    hash_table[key] = "value"
    assert hash_table[key] == "value"


def test_increase_capacity_triggers():
    hash_table = HashTable(capacity=2, load_factor_limit=0.75)
    hash_table["a"] = 1
    hash_table["b"] = 2
    assert hash_table.capacity >= 4
    assert hash_table["a"] == 1
    assert hash_table["b"] == 2


def test_collision_resolution():
    hash_table = HashTable(capacity=1)
    hash_table["a"] = 1
    hash_table["b"] = 2
    assert hash_table["a"] == 1
    assert hash_table["b"] == 2
    assert len(hash_table) == 2


def test_rehashing_keeps_all_items():
    hash_table = HashTable(capacity=2)
    items = {f"k{i}": i for i in range(10)}
    for k, v in items.items():
        hash_table[k] = v
    for k, v in items.items():
        assert hash_table[k] == v
    assert len(hash_table) == 10


def test_overwrite_does_not_increase_length():
    hash_table = HashTable()
    hash_table["a"] = 1
    length_before = len(hash_table)
    hash_table["a"] = 2
    assert len(hash_table) == length_before


def test_chained_operations():
    hash_table = HashTable()
    hash_table["x"] = 10
    hash_table["y"] = 20
    assert hash_table["x"] == 10
    hash_table["x"] = 15
    assert hash_table["x"] == 15
    del hash_table["x"]
    with pytest.raises(KeyError):
        _ = hash_table["x"]
    assert hash_table["y"] == 20
