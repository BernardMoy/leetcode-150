class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """ 
        Backtracking - but can reuse candidate and also need to maintain no duplicates

        Use an index to keep track of from which index we can choose numbers from (so numbers will be increasing order, no duplicate) 
        consider both cases of including (not advancing i) and excluding (advancing i) the candidate 
        """ 

        ans = [] 

        # i is the index onwards that we can choose numbers from (prevent duplicates) 
        # current is the current list when backtracking 
        # total is the total sum of current 
        def helper(i, current, total): 
            if total == target: 
                ans.append(current[:])
                return 
            
            # if i exceeds or total exceeds target, return 
            if total > target or i >= len(candidates): 
                return 
            
            # case that the candidate[i] is included 
            current.append(candidates[i])
            helper(i, current, total+candidates[i])  # dont advance i here as we can reuse it 

            # case that the candidate[i] is excluded
            current.pop() 
            helper(i+1, current, total)  # skip candidates[i]

            return ans 
        
        return helper(0, [], 0)