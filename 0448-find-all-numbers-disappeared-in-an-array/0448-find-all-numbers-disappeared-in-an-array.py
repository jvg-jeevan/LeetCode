class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        # iterate through the loop of length of nums 
        for i in range(1, len(nums)+1):
            # if elements not in list append to res and return
            if i not in set(nums):
                res.append(i)
        return res