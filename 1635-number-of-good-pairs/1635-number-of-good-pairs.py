class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
# good pair: equal number but not index
        good_pair = 0
# iterate through the loop and if condition is satisfied then increment the good_pair
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    good_pair += 1
        return good_pair