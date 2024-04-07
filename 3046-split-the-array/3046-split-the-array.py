class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
# # dict1 stores the occurrences of numbers, key= number, value= count
#         dict1 = {}
#         for i in set(nums):
#             dict1[i] = nums.count(i)        
# # to split into 2 lists of distinct elements  
#         return all(x <= 2 for x in dict1.values())
# # count of elements should be <= 2 all() checks the condition satisfies if all condition is True returns True or else False
        return all(nums.count(i) <= 2 for i in set(nums))