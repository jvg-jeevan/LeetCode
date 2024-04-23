class Solution:
    def singleNumber(self, nums: List[int]) -> int:
# initailize a dict() to store the occurrences of the elements
        res = {}
        for i in nums:
            res[i] = nums.count(i)
# return the key with value of 1
        return next(key for key, val in res.items() if val == 1)
# next() function to find the first key in the res dictionary where the corresponding value is equal to 1
