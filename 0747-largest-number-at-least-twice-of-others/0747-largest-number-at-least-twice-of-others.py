class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        temp = nums.copy()
        maxi = max(nums)
        nums.remove(maxi)
# make a copy of nums and remove the largest element

        result = False
# iterate throught every element
        for i in nums:
# if largest number is less than double than the number break out of loop and result as False
            if maxi < (i*2):
                result = False
                break
            else:
                result = True
# if all the elements are less than then set result as True
# if True return the index of largest num else return -1
        if result:
            return temp.index(maxi)
        else:
            return -1