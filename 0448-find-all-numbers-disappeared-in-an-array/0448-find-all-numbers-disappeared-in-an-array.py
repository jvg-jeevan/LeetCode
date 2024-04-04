class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        if not nums:
            return [1]
        nums_set = set(nums)
        # iterate through the loop of length of nums 
        for i in range(1, len(nums)+1):
            # if elements not in list append to res and return
            if i not in nums_set:
                res.append(i)
        return res