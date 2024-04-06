class Solution:
    def subtractProductAndSum(self, num: int) -> int:
        sumof = 0
        product = 1
# get each digit from number get sum and product and then get difference and return the result
        while num:
            rem = num % 10
            num//=10
            sumof += rem
            product *= rem
        return product - sumof