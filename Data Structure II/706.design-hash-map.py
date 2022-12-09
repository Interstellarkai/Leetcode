#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
class MyHashMap:
    """
    Start with empty list and dynamically resize the array
    T : O(N) 5.3% | 6868ms
    S : O(N) 97.49% | 17mb
    """

    def __init__(self):
        self.hashmap = []
        self.size = 0

    def put(self, key: int, value: int) -> None:
        flag = False
        # Try to retireve and update kv pair
        for idx in range(self.size):
            k, v = self.hashmap[idx]
            if key == k:
                self.hashmap[idx] = [key, value]
                flag = True
                break
        # Add kv pair
        if not flag:
            self.hashmap.append([key, value])
            self.size += 1

    def get(self, key: int) -> int:
        for idx in range(self.size):
            k, v = self.hashmap[idx]
            if key == k:
                return v
        return -1

    def remove(self, key: int) -> None:
        for idx in range(self.size):
            k, v = self.hashmap[idx]
            if key == k:
                del self.hashmap[idx]
                self.size -= 1
                break


class MyHashMap:
    """
    Fastest way is to either using dict, or a 10^6 in array size for each idx as key.
    Here is my solution with a small remove() optimization.
    T : O(N) 
    S : O(100 or N) 
    """

    def __init__(self):
        self.size = 100
        # each bucket is a list of pairs
        self.buckets = [[] for i in range(self.size)]

    def put(self, key: int, value: int) -> None:
        pairs = self.buckets[key % self.size]
        for idx, (k, v) in enumerate(pairs):
            if k == key:
                pairs[idx] = (key, value)
                return
        else:
            pairs.append((key, value))

    def get(self, key: int) -> int:
        pairs = self.buckets[key % self.size]
        for (k, v) in pairs:
            if k == key:
                return v
        else:
            return -1

    def remove(self, key: int) -> None:
        pairs = self.buckets[key % self.size]
        for idx, (k, v) in enumerate(pairs):
            if k == key:
                # deleting ith is O(n) cost, so lets
                # move the last one to i-th, and remove the last in O(1)
                pairs[idx] = pairs[-1]
                if idx < len(pairs):  # do not pop() if i was the last pair
                    pairs.pop()
                return

        # Your MyHashMap object will be instantiated and called as such:
        # obj = MyHashMap()
        # obj.put(key,value)
        # param_2 = obj.get(key)
        # obj.remove(key)
        # @lc code=end
