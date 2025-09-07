# Combine a dictionary for constant-time random lookups
# with doubly-linked list to store access order.
# The key value pairs are the lookup key and a
# list node as value, storing the key, value, and
# previous and next node in the doubly-linked list.
from typing import Hashable, Any, Optional


class Node:
    def __init__(self, key: Hashable, value: Any):
        self.key: Hashable  = key
        self.value: Any = value
        self.prev_node: 'Node | None' = None
        self.next_node: 'Node | None' = None


class LruCache:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.cache = {}
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head

    def _remove_node(self, node: Node):
        node.prev_node.next_node = node.next_node
        node.next_node.prev_node = node.prev_node

    def _add_to_front(self, node: Node):
        node.next_node = self.head.next_node
        node.prev_node = self.head
        self.head.next_node.prev_node = node
        self.head.next_node = node

    def _move_to_front(self, node: Node):
        self._remove_node(node)
        self._add_to_front(node)

    def get(self, key) -> Any:
        """Returns the value store for a key if present, else None."""
        # If in cache, move element to front of list and return value.
        if key in self.cache:
            node = self.cache[key]
            self._move_to_front(node)
            return self.cache[key].value
        else:
            return None

    def put(self, key, value) -> None:
        """Adds a key value pair to the LRU Cache."""
        # If in cache, update value and move Node to front of list.
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)

        # If not in cache, add to cache and add Node to front of list.
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._add_to_front(node)

            # If capacity exceeded, remove LRU element from end of list.
            if len(self.cache) > self.capacity:
                lru = self.tail.prev_node
                self._remove_node(lru)
                del self.cache[lru.key]
