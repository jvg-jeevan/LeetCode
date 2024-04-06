class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dict1 = {}
# enumerate gets index, value and iterate through the sorted elements
# when sorted the rank can be index
# dict1 key = number, value = rank
        for ind, val in enumerate(sorted(set(arr))):
            dict1[val] = ind+1
        
# result list contains rank for element that i.e value for key in dict1
        result = [dict1[i] for i in arr]

        return result