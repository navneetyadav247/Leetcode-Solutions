
# https://leetcode.com/problems/lru-cache/
# Design and implement a data structure for Least Recently
# Used cache. It should support the following operations:
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity,
# it should invalidate the least recently used item before inserting a new item.

# Dictionary stores keys with values of nodes.  
# Nodes form double linked list containing key, value pairs. 
# DLL is in order of use with least recent at head and most recent at tail. - FIFO  - Queue
# Time - O(1) to set and get
# Space - O(n)

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = null
        self.next = null

class DLL:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = tail
        self.tail.prev = head

    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def update(self, node):
        # Take out the node from exisiting position
        node.prev.next = node.next
        node.next.prev = node.prev
        # After taking out the node, put it back to tail 
        self.insert(node)

    def remove_at_head(self):
        node = self.head.next
        node.next.prev = self.head
        self.head.next = self.head.next.next
        key = node.key
        del node
        return key

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = DLL()
        self.mapping = {}

    def get(self, key):
        
        if key not in self.mapping:
            return -1

        node = self.mapping[key]
        # Update queue and move node to tail
        self.queue.update(node)
        return node.value

    def set(self, key, value):
        
        # Update value, update queue and move node to tail
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value
            self.queue.update(node)
            return

        node = Node(key, value)
        self.mapping[key] = node
        self.queue.insert(node)

        # If cache is full, eject oldest 
        if capacity == 0 :
            removed_key = self.queue.remove_at_head()
            del self.mapping[removed_key]
        else:
            self.capacity -= 1 


