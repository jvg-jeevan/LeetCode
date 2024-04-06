class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = dec = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                inc = False
                break
        for x in range(len(nums)-1):
            if nums[x] < nums[x+1]:
                dec = False
                break
        return inc or dec