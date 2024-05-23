class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bubble sort technique
# i -> from 0th to last-1 element
        for i in range(len(nums)-1):
# j -> from 1st element to last element
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    # swap the numbers if pervious is greater than next
                    nums[i], nums[j] = nums[j], nums[i]