# Combine a dictionary for constant-time random lookups
# with doubly-linked list to store access order.
# The key value pairs are the lookup key and a
# list node as value, storing the key, value, and
# previous and next node in the doubly-linked list.
import time
from threading import Lock
from typing import Hashable, Any


class Node:
    def __init__(self, key: Hashable | None, value: Any):
        self.key = key
        self.value = value
        self.prev_node: 'Node | None' = None
        self.next_node: 'Node | None' = None
        self.start_of_life = time.time()


class LruCache:
    """LRU Cache with optional time to life.

    TTL defaults to 0 which means unlimited TTL.
    """

    def __init__(self, capacity: int, ttl_in_seconds=0):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.cache = {}
        self.capacity = capacity
        self.ttl = ttl_in_seconds
        self.head = Node()
        self.tail = Node()
        self.head.next_node = self.tail
        self.tail.prev_node = self.head
        self.lock = Lock()

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
        """Returns the value store for a key if present, else None.

        If TTL is used, the method performs lazy cache eviction
        for expired elements.
        """
        # If in cache, move element to front of list and return value.
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                if self.ttl == 0 or time.time() - node.start_of_life <= self.ttl:
                    self._move_to_front(node)
                    return node.value
                else:
                    del self.cache[key]
            return None

    def put(self, key, value) -> None:
        """Adds a key value pair to the LRU Cache."""
        with self.lock:
            # If in cache, update value and move Node to front of list.
            if key in self.cache:
                node = self.cache[key]
                node.value = value
                node.start_of_life = time.time()
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
