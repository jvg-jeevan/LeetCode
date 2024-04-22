class Solution:
    def factorial(self, n):
        return n * factorial(n-1)
    def trailingZeroes(self, n: int) -> int:
        # fact = 1
        # for i in range(1, n+1):
        #     fact *= i
        if n > 0:
            fact = self.factorial(n)
        else:
            fact = 1
        result = 0
        while fact > 9:
            if fact % 10 == 0:
                result += 1
                fact//= 10
            else:
                break
        return result