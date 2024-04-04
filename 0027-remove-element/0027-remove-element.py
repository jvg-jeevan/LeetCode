class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums[:] = [x for x in nums if x!=val]
        # nums[:] is used to modify the nums in place instead of creating the new list
        # if the number x is not equal to the value specified then add that to nums in other words removing the val specified
        return len(nums)
        # return the length of nums