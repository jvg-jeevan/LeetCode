class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
# take the first element as minimum
        mini = nums[0]
# iterate through all the elements other than 1st element 
        for i in nums[1:]:
            # if element is less than mini then return mini
            if i < mini:
                return i
        return mini