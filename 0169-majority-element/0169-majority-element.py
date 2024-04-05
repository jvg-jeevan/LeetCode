class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # countof = 0
        # for i in set(nums):
        #     x = nums.count(i)
        #     if x > countof:
        #         countof = x
        #         element = i
        # return  element
        x = len(nums) / 2
        # the given condition is that count of number will be greater than (n/2)
        for i in set(nums):
            # if count of number is greater than the condition then return number
            if nums.count(i) >= x:
                return i