class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if number is zero it cannot be power of two
        if n == 0:
            return False

        while n > 0:
            # n will be 1 for pow(2, 0)
            if n == 1:
                return True
            # if remainder of number by 2 is not zero then it cannot be pow(2)
            if n%2 != 0:
                break
            # divide by 2 and assign the number
            n//=2
        return False