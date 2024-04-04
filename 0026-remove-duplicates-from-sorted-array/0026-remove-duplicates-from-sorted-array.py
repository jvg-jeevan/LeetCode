class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        # convert the list to set (to remove the duplicate items) and then sort them in ascending order 
        return len(nums)
        # return the length of new list nums