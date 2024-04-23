class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
# as the largest element will be greater than the neighbors so return the index
        return nums.index(max(nums))