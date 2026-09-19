# Key idea: Follow how inputs are transformed into the returned result or updated data structure.
# Group the state and operations used by the design hashset implementation.
class MyHashSet:

    # Initialize the state needed by a new instance.
    def __init__(self):
        self.hash_set = set()

    # Compute or update the add result for the supplied input.
    def add(self, key: int) -> None:
        # Choose this path when `key not in self.hash_set` is true.
        if key not in self.hash_set:
            self.hash_set.add(key)

        

    # Compute or update the remove result for the supplied input.
    def remove(self, key: int) -> None:
        # Choose this path when `key in self.hash_set` is true.
        if key in self.hash_set:
            self.hash_set.remove(key)

    # Compute or update the contains result for the supplied input.
    def contains(self, key: int) -> bool:
        # Choose this path when `key in self.hash_set` is true.
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