class Solution:
    def findMaxK(self, nums: List[int]) -> int:
# if the length of the nums becomes zero then return -1
        if len(nums) == 0:
            return -1
# get the maximum of nums
        maximum = max(nums)

# if negative of maximum exist in nums return the maximum
        if (0 - maximum) in nums:
            return maximum
# if negative not exist remove the element from list 
        else:
            nums.remove(maximum)
# call the function recursively until both pos and neg of max is found
            return self.findMaxK(nums)