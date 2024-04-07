class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        result = 0
        # iterating through all the elements
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                # given condition
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        result += 1
        return result