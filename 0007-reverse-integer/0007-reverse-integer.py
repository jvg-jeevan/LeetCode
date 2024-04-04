class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        # reverse the number
        if x >= 0:
            x = int(str(x)[::-1])
            # convert to str and reverse and convert back to int
        else:
            x = -int(str(-x)[::-1])
            # conver to positive x and then reverse the str and then convert back to negative int
        
        if x <= INT_MIN or x >= INT_MAX:
            return 0
            # if reversed number x is out of range then return 0
        else:
            return x
            # else return the number