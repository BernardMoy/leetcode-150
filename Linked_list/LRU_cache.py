class Node: 
    def __init__(self, key, val): 
        self.key = key 
        self.val = val 
        self.prev = None  
        self.next = None 

class LRUCache:
    """ 
    Using a queue to store the (key, call counts) pair take O(log n) time to retrieve 

    Maintain a doubly linked list, where oldest accessed items are on the left and more recently ones are to the right
    There are one dummy node on both sides

    The remove function removes the node from the LL by inspecting its prev and next elements
    and the insert function inserts the node at the rightmost (= most recent)

    Finally, the d dictionary stores key:Node pairs so that every node can be accessed in constant time (values / vals are stored inside the nodes instead of directly in values of the dictionary) 
    """ 
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.d = {} 

        # Maintain a pointer to the leftmost and rightmost DUMMY nodes
        self.left = Node(0,0) 
        self.right = Node(0,0) 

        # Connect the leftmost and rightmost dummy nodes 
        self.left.next = self.right 
        self.right.prev = self.left 

    def get(self, key: int) -> int:
        if key in self.d: 
            # By removing and re-inserting the key, the key is pushed to the rightmost 
            self.remove(self.d[key])
            self.insert(self.d[key])
            return self.d[key].val
        
        # not found 
        return -1 

    def put(self, key: int, value: int) -> None:
        # Override pre-existing values by deleting them 
        if key in self.d: 
            self.remove(self.d[key]) 
        node = Node(key, value) 
        self.d[key] = node
        self.insert(node)  # Re-insert (or insert) the node at the rightmost 

        # check if length of cache exceeds capacity 
        if len(self.d) > self.capacity: 
            # remove the leftmost key using the remove function (left.next bc left is dummy)
            t = self.left.next 
            self.remove(t)

            # also remove it from the d by passing key 
            del self.d[t.key] 

    # Custom remove method
    # Takes a node pointer, and remove it from the doubly linked list (For ejecting) 
    def remove(self, node): 
        # Extract the prev and next of the node and join them together 
        p, n = node.prev, node.next 
        p.next = n 
        n.prev = p
    
    # Custom insert method 
    # Takes a node pointer, and insert that node at the rightmost position (For adding) 
    def insert(self, node): 
        p, n = self.right.prev, self.right 
        p.next = node 
        n.prev = node
        node.next = n  # Maintain n as the rightside dummy node 
        node.prev = p 

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)