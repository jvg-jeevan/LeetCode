class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# dict1 stores the occurrences of the elements in nums
        dict1 = {}
        for i in set(nums):
            dict1[i] = nums.count(i)
# sort the dict1 as per values
        dict1 = dict(sorted(dict1.items(), key= lambda item: item[1], reverse=True))
        res = list(dict1.keys())
        return res[:k]        