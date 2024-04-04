class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for i in range(1, len(nums)+2):
            # iterate through the loop with elements (+ve) from 1 to length of list +1 to take all possible +ve elements
            if i not in nums_set:
                return i
                # if element is not found return the element
        return 1