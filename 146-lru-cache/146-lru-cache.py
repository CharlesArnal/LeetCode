class LRUCache:
    # Only works if we consider that capacity is O(1)
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keys = []
        self.kv_dict = {}

    def get(self, key: int) -> int:
        if key in self.kv_dict:
            self.keys.remove(key)
            self.keys.append(key)
            return self.kv_dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv_dict:
            self.kv_dict[key] = value
            self.keys.remove(key)
            self.keys.append(key)
        else:
            if len(self.keys)>=self.capacity:
                self.kv_dict.pop(self.keys[0])
                self.keys.remove(self.keys[0])
            self.keys.append(key)
            self.kv_dict[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)