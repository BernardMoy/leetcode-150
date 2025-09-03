class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """ 
        Links can be modelled by a graph: if a/b = 3, then a --3--> b and b --1/3--> a
        Find the total multiplied weight from source to destination for each query. 
        
        Perform a BFS from a source to find the destination by linear iteration
        with a queue storing the current node and current weight. 
        """ 

        adj = defaultdict(list)   # directed graph -- source: [(dest, weight)]

        for i in range(len(equations)): 
            src, dest = equations[i] 
            adj[src].append((dest, values[i]))
            adj[dest].append((src, 1/values[i]))
        
        ans = [] 

        def bfs(src, dest): 
            # handle nodes that are not in the graph 
            if src not in adj or dest not in adj: 
                return -1 

            # keep track of the current node and the multiplied edges in a queue 
            q = deque([(src, 1)])
            visited = set() 
            while q: 
                node, weight = q.popleft() 
                if node == dest:  
                    return weight 

                # prevent loops 
                if node in visited: 
                    continue 
                
                # append neighbours 
                for node2, weight2 in adj[node]: 
                    q.append((node2, weight2*weight))
                
                visited.add(node)
            
            return -1 

        for a,b in queries: 
            ans.append(bfs(a,b)) 
        
        return ans 