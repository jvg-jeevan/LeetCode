class Solution:
    def findNumbers(self, nums: List[int]) -> int:
# res to store the count
        res = 0
# for each element in nums
        for num in nums:
# if length of element is even increment res
            if len(str(num)) % 2 == 0:
                res += 1
# return the count res
        return res