class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n ==1:
            return True
        for i in range(0,100):
            if 2**i == n:
                return True

        return False
