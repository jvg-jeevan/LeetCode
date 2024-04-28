class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
# sort the list nums
        nums.sort()
# instead of removing the elements, the number will be after index of k i.e  index number of steps to get k
        if k in nums:
            return nums.index(k)
        res = 0
        for i in range(len(nums)-1):
            if k > nums[i+1] and k < nums[i]:
                res = i
        return res