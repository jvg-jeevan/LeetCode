class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) < 3:
            return nums[-1]
        return nums[-3]
# convert the list to set to remove duplicate entries
# and sorted() returns the list 
# if the length of list is less than 3 then the last element will be greatest
# if not return the last 3rd element from list