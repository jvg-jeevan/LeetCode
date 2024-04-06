class Solution:
    def isPowerOfFour(self, n: int) -> bool:
# negative and zero cannot be a pow() of any number
        if n <= 0:
            return False
# when number is greater than zero and if number becomes 1 on continuous division without leaving out any remainder will the pow() of any number
        while n > 0:
            if n == 1:
                return True
            elif n%4 != 0:
                break
            n //= 4
        return False