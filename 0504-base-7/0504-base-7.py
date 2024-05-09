class Solution:
    def convertToBase7(self, num: int) -> str:

# if num is zero then return '0'
        if num == 0: return '0'

# get the absolute value of num if -ve number exist
        n = abs(num)

# res stores the str value of base 7
        res = ''
        while n > 0:
            res += str(n % 7)
            n //= 7

# if num is -ve then add - to res
        if num < 0:
            res += '-'

# return the reverse of res 
        return res[::-1]