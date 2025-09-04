class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """ 
        Contrary to course schedule I here each prerequisite POINT TO courses 
        hence the problem become finding a valid topo sort 

        Start with in degree 0, consider their neighbours, 
        and add them to queue if they become in degree 0 after removing current node. 

        Handle the impossible situation in the end -> not necessarily related to course schedule I 
        """ 

        # in the graph PREREQUISITES POINT TO COURSES 
        d = defaultdict(list) 
        degs = defaultdict(int) 
        for a,b in prerequisites: 
            d[b].append(a)   # b --> a 
            degs[a] += 1 
        
        # store all current nodes already with in degree = 0 (or not in degs, i.e. not pointed) 
        # and expand from there 
        q = deque([i for i in range(numCourses) if i not in degs or degs[i] == 0])
        ans = [] 

        while q: 
            cur = q.popleft() 
            ans.append(cur) 

            # delete that node with no in neighbours, and add neighbours
            # if they become in degree = 0 after that. 
            for nei in d[cur]: 
                degs[nei] -= 1 
                if degs[nei] == 0: 
                    q.append(nei) 
        
        # handle the not possible case here 
        return ans if len(ans) == numCourses else [] 

        
        