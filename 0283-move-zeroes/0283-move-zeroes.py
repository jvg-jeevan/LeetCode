class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == 0:
        #             nums[i], nums[j] = nums[j], nums[i]
        # print(nums)

        # initialize index of zero as 0
        zero = 0
        # iterate through the elements using index
        for i in range(len(nums)):
            # if element at index i is non zero 
            if nums[i] != 0:
                # swap the element at i with element at zero
                nums[i], nums[zero] = nums[zero], nums[i]
                # increment the index of zero
                zero += 1