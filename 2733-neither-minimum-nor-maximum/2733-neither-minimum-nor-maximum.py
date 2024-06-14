class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
# sort the numbers
        nums.sort()
# if length is less than 3 i.e there will be max and min element only so return -1
        if len(nums) < 3:
            return -1
# return any element in between i.e element at index 1
        return nums[1]