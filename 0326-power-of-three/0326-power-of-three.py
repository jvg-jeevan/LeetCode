class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 0:
            if n == 1:
                return True
            elif n%3 != 0:
                break
            n //= 3
        return False