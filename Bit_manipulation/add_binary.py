class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Simulate adding binary numbers
        using carry
        and current position = (d1+d2+carry)
        """

        ans = ""
        carry = 0

        # Iterate strings backwards
        a = a[::-1]
        b = b[::-1]

        for i in range(max(len(a), len(b))):
            d1 = 0
            d2 = 0

            if i < len(a):
                d1 = int(a[i])
            if i < len(b):
                d2 = int(b[i])

            char = (d1 + d2 + carry) % 2
            carry = (d1 + d2 + carry) // 2
            ans += str(char)

        # Add the final carry if any
        if carry:
            ans += "1"

        return ans[::-1]
