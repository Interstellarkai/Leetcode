#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
import collections


class LRUCache:
    """
    T : O(N)
    S : O(N)
    """

    def __init__(self, capacity):
        self.dic = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.dic:  # O(N)
            return -1
        # The newest item is at the end of the OrderedDict
        v = self.dic.pop(key)
        self.dic[key] = v   # set key as the newest one
        return v

    def set(self, key, value):
        # Key is already in the dictionary
        if key in self.dic:  # O(N)
            self.dic.pop(key)
        else:
            # Is there space for the new item?
            if self.capacity > 0:
                self.capacity -= 1
            else:  # self.dic is full
                self.dic.popitem(last=False)  # Remove first item
        self.dic[key] = value


"""
https://leetcode.com/problems/lru-cache/discuss/352295/Python3-doubly-linked-list-and-dictionary
The most frequent operation of the problem is changing the node position in the list.
Change position of the node means two operations, delete and insert.
    1. Double linked list data structure takes constant time O(1) to insert or delete nodes a linked list by repointing the previous and next pointer of the node.
    2. Array data structure takes O(n) to insert or delete an element in the list by shifting all the element behind the position (backward for insertion, forward for deletion) by one.

put :
    1. if the key is already in the cache, we update the value, remove the key node and insert the key node after the head;
    2. if the key is not in cache, if the cache is not full,we insert the new key node after the head. If the cache is full, we delete the node before the tail to make room for the new key node, and insert the new key node after the head.

get:
    1. return the value of the key.
    2. remove the key node.
    3. insert the key node after the head.
"""


class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()  # key to node
        self.capacity = capacity
        self.head = ListNode(0, 0)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:             # similar to get()
            node = self.dic[key]
            self.removeFromList(node)
            self.insertIntoHead(node)
            node.value = value         # replace the value len(dic)
        else:
            if len(self.dic) >= self.capacity:
                self.removeFromTail()
            node = ListNode(key, value)
            self.dic[key] = node
            self.insertIntoHead(node)

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertIntoHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = headNext
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeFromList(tail_node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
