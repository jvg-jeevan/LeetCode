class Solution:
    def triangleType(self, nums: List[int]) -> str:
# convert to set to check for duplicates
        num_set = set(nums)
        num_length = len(num_set)
# unpacking the list
        a, b, c = nums
# if the sum of length of two sides are less than other side then none
        if not(a<b+c and b<a+c and c<b+a):
            return 'none'
# if length of 2 sides are equal then isosceles
        if num_length == 2:
            return 'isosceles'
# if all are same then equilateral
        if num_length == 1:
            return 'equilateral'
        return 'scalene'
# return scalene if all sides are not equal and noy meet all condition