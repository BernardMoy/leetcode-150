class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        """
        Classic BFS queue, with a function is_diff_one to determine if each element in bank
        is a direct neighbour (1 mutation) with the current element, 
        thus avoid creating a full graph. 
        """
        def is_diff_one(a,b): 
            count = 0 
            for i in range(len(a)): 
                if a[i] != b[i]: 
                    count += 1 
                    if count == 2: 
                        return False 
            return count == 1 
        
        # use a queue for BFS 
        q = deque([startGene])
        visited = set([startGene]) 
        ans = 0 
        while q: 
            for _ in range(len(q)): 
                cur = q.popleft() 
                if cur == endGene: 
                    return ans 
                for b in bank: 
                    if b not in visited and is_diff_one(cur, b): 
                        visited.add(b) 
                        q.append(b) 
        
            # for one level traversed, add one to ans 
            ans += 1 
        
        return -1