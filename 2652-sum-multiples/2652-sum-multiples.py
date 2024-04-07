class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sumof = 0
# add the numbers that are divisible by 3, 5, 7, 9 and return sum
        for i in range(1, n+1):
            if (i%3 == 0) or (i%5 == 0) or (i%7 == 0) or (i%9 == 0):
                sumof += i 
        return sumof