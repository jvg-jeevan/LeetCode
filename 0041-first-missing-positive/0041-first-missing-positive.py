class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1

        nums_set = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums_set:
                return i
