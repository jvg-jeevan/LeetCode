class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # for all the element go through the loop
        for ind in range(len(nums)):
        # if sum to left is equal to sum to right (ind+1) to last element 
            if sum(nums[:ind]) == sum(nums[ind+1:]):
                # if True return index
                return ind
        # else return -1
        else:
            return -1