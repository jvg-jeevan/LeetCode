class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # for numbers <= 0 pow(3) does not exist
        if n <= 0:
            return False

        while n > 0:
# when number becomes 1 after continuously being divided by 3 is a pow(3)
            if n == 1:
                return True
            # if remainder not zero false
            elif n%3 != 0:
                return False
            n //= 3
            # divide the number and get numerator