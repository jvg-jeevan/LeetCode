class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
# i, j takes through all the elements
        for i in range(len(nums)):
            for j in range(len(nums)):
# check if the condition satisfies return index [i, j]
                if (abs(i-j) >= indexDifference) and (abs(nums[i]-nums[j]) >= valueDifference):
                    return [i, j]
# if no such index found then return [-1, -1]
        return [-1, -1]