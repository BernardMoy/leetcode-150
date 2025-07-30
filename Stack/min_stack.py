class MinStack:
    """
    Use a minstack to keep track of previous min elements
    remember to store duplicates in case there are multiple occurrnces of the min element. 
    """ 

    def __init__(self):
        self.stx = [] 
        self.minstx = [] 

    def push(self, val: int) -> None:
        self.stx.append(val) 
        if not self.minstx or val <= self.minstx[-1]: 
            self.minstx.append(val) 
        

    def pop(self) -> None:
        val = self.stx.pop() 
        if val == self.minstx[-1]: 
            self.minstx.pop() 

    def top(self) -> int:
        return self.stx[-1]

    def getMin(self) -> int:
        return self.minstx[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()