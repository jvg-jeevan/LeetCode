class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
# intitalize the result
        result = 0
# if sum of the numbers is strictly less than target then increment the result
        for i in range(len(nums) - 1):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j]) < target:
                    result += 1
        return result
    