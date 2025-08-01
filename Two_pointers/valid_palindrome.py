class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Classic
        """
        # Modify the string
        sx = "".join([x.lower() for x in s if x.isalpha() or x.isdigit()])

        # Two pointers to check palindrome
        for i in range(ceil(len(sx) / 2)):
            if sx[i] != sx[len(sx) - i - 1]:
                return False

        return True
