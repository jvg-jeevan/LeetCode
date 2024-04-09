class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
    # if nums length=1 then return str of num
        if len(nums) == 1:
            return str(nums[0])
    # if len=2 then return str of a / b
        if len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])
    # if len is greater than 2 then a/(b/c/d.......)
        return str(nums[0]) + '/(' + '/'.join(list(map(str, nums[1:]))) + ')'
# here joining the string part of 1st number and then concatenating () and joining / between the numbers