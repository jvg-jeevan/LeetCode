class Solution:
    def isThree(self, n: int) -> bool:
# check how many divisors does the number have
        result = 0
        for i in range(1, n+1):
            if n % i == 0:
                result += 1
# return result if it has olny 3 divisors
        return result == 3