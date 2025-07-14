class RandomizedSet:
    """
    Simulate a set using an array and a dictionary (For indexing)
    Such that random.choice() can run on a set
    without having to first convert set to an array for this operation

    When removing element, instead of shifting all the indices of the latter elements, 
    swap with the last element and remove the last element. 
    """
    def __init__(self):
        self.a = [] 
        self.d = {}

    def insert(self, val: int) -> bool:
        if val not in self.d:
            self.a.append(val) 
            self.d[val] = len(self.a)-1
            return True 
        else: 
            return False 

    def remove(self, val: int) -> bool:
        if val in self.d:
            index = self.d[val] 
            last_elem = self.a[-1] 

            # Swap with last element 
            self.d[val], self.d[last_elem] = self.d[last_elem], self.d[val]
            self.a[-1], self.a[index] = self.a[index], self.a[-1]

            # Remove last element 
            self.a.pop() 
            del self.d[val]
            return True 
        else: 
            return False 

    def getRandom(self) -> int:
        return random.choice(self.a)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()