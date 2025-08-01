class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Add the translation when the direction (largest to smallest) is correct,
        else subtract it.
        Use a current variable to keep track of them
        """

        translations = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        current = -float("inf")
        ans = 0
        for n in s[::-1]:
            if translations[n] >= current:
                ans += translations[n]
            else:
                ans -= translations[n]

            # Set current
            current = translations[n]

        return ans
