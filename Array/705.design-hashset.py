# This wraps Python's built-in set rather than implementing buckets, hashing, or collision handling.
# Membership, insertion, and removal are expected O(1); space grows with distinct stored keys.
class MyHashSet:

    def __init__(self):
        self.hash_set = set()

    # Set insertion is idempotent: repeated adds should leave one copy of a key.
    def add(self, key: int) -> None:
        if key not in self.hash_set:
            self.hash_set.add(key)

        

    # The membership guard makes removing an absent key a no-op instead of raising KeyError.
    def remove(self, key: int) -> None:
        if key in self.hash_set:
            self.hash_set.remove(key)

    # Report whether the key is currently stored; previous removals must be reflected.
    def contains(self, key: int) -> bool:
        if key in self.hash_set:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

myHashSet  =  MyHashSet()
myHashSet.add(1)
myHashSet.add(2)
myHashSet.contains(1);
myHashSet.contains(3); 
myHashSet.add(2);      
myHashSet.contains(2); 
myHashSet.remove(2);  
myHashSet.contains(2); 