class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """ 
        use a single count variable to store the max element's occurrnce
        when encounter the max element, count += 1, else count -= 1. 
        Since it appears more than n/2 times, count should nver be zero
        if the correct majority element is chosen. 
        """ 
        
        count = 0
        cur = ''

        for n in nums:
            if cur == n:
                count += 1
            
            elif count == 0:
                cur = n
            
            else:
                count -= 1

        return cur