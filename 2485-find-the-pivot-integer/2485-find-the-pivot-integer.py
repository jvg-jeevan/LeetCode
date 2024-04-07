class Solution:
    def pivotInteger(self, n: int) -> int:
# create a list that contains numbers in range(n)
        nums = list(range(1, n+1))
# iterate through the loop and check if sum of elements to left and right are same return the element (i) is index (i+1) is number
        for i in range(len(nums)):
            if sum(nums[:i+1]) == sum(nums[i:]):
                return i+1
# if not found return -1
        return -1