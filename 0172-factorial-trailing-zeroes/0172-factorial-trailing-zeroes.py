class Solution:
# get the factorial using recursion
    def factorial(self, n):
        return n * factorial(n-1)
    
    def trailingZeroes(self, n: int) -> int:
# positive number then get factorial
        if n > 0:
            fact = self.factorial(n)
        else:
            fact = 1
# result to store the count of trailing zeros
        result = 0
# if last number is not divisible by 10 then no trailing zeros so return 0
        if fact % 10 != 0:
            return result
    # if fact > 9 then check for last zero until > 9
        while fact > 9:
# if last digit is zero then increment result and divide fact bt 10
            if fact % 10 == 0:
                result += 1
                fact//= 10
# if not divisible by 10 then break
            else:
                break
        return result