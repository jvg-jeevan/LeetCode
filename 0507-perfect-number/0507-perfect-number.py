class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
# returns False because 1 is not considered a perfect number
            return False
# used to accumulate the sum of the divisors of num
        sumof = 1
# loop from 2 to square root of num
        for i in range(2, int(num ** 0.5)+1):
# if a i divides number completely
            if num % i == 0:
# add the sum of divisors is updated by adding both i and num // i to sumof. This effectively adds the pair of divisors (i, num//i) to the sum
                sumof += (i + num//i)
# return if obtained sum is equal to num
        return sumof == num