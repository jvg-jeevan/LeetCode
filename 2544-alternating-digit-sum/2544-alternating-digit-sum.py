class Solution:
    def alternateDigitSum(self, n: int) -> int:
# initialize res to store the sum
        res = 0
# convert n from int to nums (list of int)
        nums = list(map(int, str(n)))
# iterate through each index of list nums
        for i in range(len(nums)):
# if index is even add num to res
            if i % 2 == 0:
                res += nums[i]
# if odd subtract num from res
            else:
                res -= nums[i]
# return the res
        return res