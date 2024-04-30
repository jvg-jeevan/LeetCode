class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        sumof = 0
        for i in range(1, (num//2)+1):
            if num % i == 0:
                sumof += i
        return sumof == num