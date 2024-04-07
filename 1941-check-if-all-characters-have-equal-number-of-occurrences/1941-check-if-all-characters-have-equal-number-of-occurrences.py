class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
# sorted(s) creates a sorted list by the characters in string
        arr = sorted(s)
# dict1 to store the occurrences
        dict1 = {}
        for i in set(arr):
            dict1[i] = arr.count(i)
# set() removes duplicate elements and if lenght of that is 1 then all values will be same
        return len(set(dict1.values())) == 1