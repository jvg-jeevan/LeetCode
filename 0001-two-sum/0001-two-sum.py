class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iterate through the list elements
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                # if sum of two numbers in list is equal to target then return the index
                if (nums[i] + nums[j]) == target:
                    return [i, j]
        # if no such pair found return empty list
        return []