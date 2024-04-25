class Solution:
    def largestNumber(self, nums: List[int]) -> str:
# convert type of element from int to str
        nums = list(map(str, nums))
# sort the list in reverse order (lambda func concatenates the string 10 times and compares with them to get them in reverse sorted order)
        nums.sort(key= lambda z: z*10, reverse= True)
# if the 1st number is 0 then number will be zero
        if nums[0] == '0':
            return '0'
# return the str of the sorted nums
        return ''.join(nums)