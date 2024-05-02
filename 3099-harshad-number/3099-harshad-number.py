class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
# get the sum of all digits using sum()
        num_sum = sum(list(map(int, str(x))))
# if x is completely divisible by sum return sum
        if x % num_sum == 0:
            return num_sum
# if not divisible then return -1
        else:
            return -1