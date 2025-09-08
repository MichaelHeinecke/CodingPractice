# Use one dict to map keys to value and frequency tuples.
# Use second dict to map frequencies to order dicts of
# keys, functioning as frequency buckets.
# Variable is used to track the minimum frequency in stored.
# If capacity is exceeded, oldest element (first in order dict)
# in respective frequency bucket is removed.
from collections import OrderedDict, defaultdict
from typing import Any


class LFUCache:
    """LFU Cache.

    LFU element evicted is the oldest element with
    minimum frequency.
    """

    def __str__(self) -> str:
        return str(
            f"Keys to val freq: {self.key_to_val_freq}, freq to keys: {self.freq_to_keys}")

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
        self.capacity = capacity
        self.key_to_val_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0

    def _update_freq(self, key):
        # Update freq in key_to_val_freq
        val, freq = self.key_to_val_freq[key]
        self.key_to_val_freq[key] = (val, freq + 1)
        # Move to next higher freq bucket in freq_to_keys
        del self.freq_to_keys[freq][key]
        # Delete bucket if empty
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
        self.freq_to_keys[freq + 1][key] = None
        # Update min_freq
        if freq == self.min_freq and not self.freq_to_keys[freq]:
            self.min_freq += 1

    def get(self, key) -> Any:
        """Returns the value stored for a key if present, else None."""
        if key in self.key_to_val_freq:
            self._update_freq(key)
            return self.key_to_val_freq[key][0]
        return None

    def put(self, key, value) -> None:
        """Adds or updates a key value pair in the LFU Cache."""
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
        else:
            # Evict prior to inserting new element to avoid deleting the new element
            if len(self.key_to_val_freq) >= self.capacity:
                lfu_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[lfu_key]

            self.key_to_val_freq[key] = (value, 1)
            # OrderedDict is only used to stored keys in order of insertion
            self.freq_to_keys[1][key] = None
            self.min_freq = 1


if __name__ == '__main__':
    cache = LFUCache(3)
    cache.put("A", "some value")
    cache.get("A")
    cache.put("B", "some value")
    cache.get("B")
    cache.put("C", "some value")
    cache.put("D", "some value")

    print(cache)
