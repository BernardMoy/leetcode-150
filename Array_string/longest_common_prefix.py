class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        To check if all elements position of a list are equal,
        compare them using all() to the first element of the list.
        """
        index = 0
        for i in range(min([len(x) for x in strs])):
            if all(x[i] == strs[0][i] for x in strs):
                index += 1
            else:
                return strs[0][:index]  # Break early - this is required
        return strs[0][:index]
