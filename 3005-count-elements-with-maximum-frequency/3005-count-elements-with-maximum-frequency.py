class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        dict1 = {}
        res = 0
# dict1 contains occurrences, key = number, values= occurrences
        for i in set(nums):
            dict1[i] = nums.count(i)
# max_val contains maximum value in dict1
        max_val = max(dict1.values())
# add the count(key) to res with maximum value 
        for key, value in dict1.items():
            if value == max_val:
                res += nums.count(key)
        return res
# return the result