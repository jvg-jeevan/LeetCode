from collections import Counter
class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
# sort() the nums list in reverse order
        nums.sort(reverse=True)
# Counter() returns a dict(), key= num, value= occurrences
        res = Counter(nums)
# sort the res dict based on values
        res = dict(sorted(res.items(), key= lambda items: items[1]))
# ans to store the result
        ans = []
# for each item in res extend the ans list with value number of keys
        for key, val in res.items():
            ans.extend([key]*val)
# return the result ans
        return ans