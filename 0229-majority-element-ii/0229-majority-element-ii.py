class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # the given condition
        n = len(nums)/3
        
        # list to store result 
        result = []

        for i in set(nums):
            # if count of number is greater than condition add element to result
            if nums.count(i) > n:
                result.append(i)
        return result