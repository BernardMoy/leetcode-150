class Solution:
    def singleNumber(self, nums: List[int]) -> int: 
        """
        Using a dictionary gets accepted
        """
        return [key for key, value in Counter(nums).items() if value == 1][0]