class Solution:
    def reverseBits(self, n: int) -> int:
        """ 
        Use [2::] to extract the binary number part and use .zfill(32) to add leading zeroes 
        """ 
        b = bin(n)[2:].zfill(32)  # Fill all leading zeroes until length is 32
        r = b[::-1]
        return int(r, 2)
