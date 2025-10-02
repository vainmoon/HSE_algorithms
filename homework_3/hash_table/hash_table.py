from collections.abc import Hashable


class HashTableNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, load_factor_limit: float = 0.75, capacity: int = 4):
        self.capacity = capacity
        self.data = [[] for _ in range(self.capacity)]
        self.elements_num = 0
        self.load_factor_limit = load_factor_limit

    def _get_load_factor(self) -> int:
        return self.elements_num / self.capacity

    def _hash(self, key: Hashable) -> int:
        return hash(key) % self.capacity

    def _get_bucket_idx(self, key: Hashable) -> int | None:
        bucket_list = self.data[self._hash(key)]
        for i, hash_table_node in enumerate(bucket_list):
            if hash_table_node.key == key:
                return i
        return None

    def _increase_capacity(self) -> None:
        self.capacity *= 2
        past_data = self.data
        self.data = [[] for _ in range(self.capacity)]
        for bucket_list in past_data:
            for hash_table_node in bucket_list:
                self.data[self._hash(hash_table_node.key)].append(hash_table_node)

    def __len__(self) -> int:
        return self.elements_num

    def __getitem__(self, key: Hashable) -> object:
        bucket_list = self.data[self._hash(key)]
        bucket_idx = self._get_bucket_idx(key)
        if bucket_idx is None:
            raise KeyError(key)
        return bucket_list[bucket_idx].value

    def __setitem__(self, key: Hashable, value: object) -> None:
        bucket_list = self.data[self._hash(key)]
        bucket_idx = self._get_bucket_idx(key)
        if bucket_idx is None:
            self.elements_num += 1
            bucket_list.append(HashTableNode(key, value))
            if self._get_load_factor() >= self.load_factor_limit:
                self._increase_capacity()
            return

        bucket_list[bucket_idx].value = value

    def __delitem__(self, key: Hashable) -> None:
        bucket_list = self.data[self._hash(key)]
        bucket_idx = self._get_bucket_idx(key)
        if bucket_idx is None:
            raise KeyError(key)
        del bucket_list[bucket_idx]
        self.elements_num -= 1
