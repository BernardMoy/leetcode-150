class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """ 
        Build a graph where each NODE POINTS TO its pre-requisites 
        return False if cycle exists (cant be completed). 

        Standard 2 sets way to check for cycles using DFS 
        visited -> cache already visited nodes (-> NO CYCLE if in this set) 
        recursionStack -> cache currently visiting nodes (-> HAVE CYCLE if in this set)
        """ 

        # in the graph each current node points to its pre requisites 
        d = defaultdict(list) 
        for a,b in prerequisites: 
            d[a].append(b) 
        
        # dfs to find cycles with a starting node (return True if cycles)
        # similar to connected components: Add all neighbours while tracking already visited nodes
        visited = set() 
        recursionStack = set() 
        def dfs(start): 
            if start not in d: 
                return False 
            
            # in current rec stack -> cycle 
            if start in recursionStack: 
                return True 
            
            # previously visited -> return False 
            if start in visited: 
                return False 
            
            recursionStack.add(start) 
            for nei in d[start]: 
                if dfs(nei): 
                    return True 
            recursionStack.remove(start) 

            visited.add(start)
            return False 

        # run dfs starting at each node 
        for course in range(numCourses):
            if dfs(course): 
                return False  
        
        return True 