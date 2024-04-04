class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
            # if element found return index
        else:
            # if element is greater than the max element then add at the end i.e len(nums) becomes the last element
            if target > max(nums):
                return len(nums)
            # iterate through the loop
            for i in range(len(nums)):
                # if target is less than the current element then return the current index
                if target < nums[i]:
                    return i
                # if element is greater than current and less than next element return next index
                elif target > nums[i] and target < nums[i+1]:
                    return i+1