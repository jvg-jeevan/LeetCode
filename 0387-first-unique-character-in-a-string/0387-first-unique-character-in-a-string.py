class Solution:
    def firstUniqChar(self, s: str) -> int:
# create a dict to store the frequency of elements i.e count of elements
        dict1 = {}
# key = string literal, value = count of that string
        for i in set(s):
            dict1[i] = s.count(i)
# enumerate is used to iterate using both the index and values of the iterable 
        for ind, val in enumerate(s):
            if dict1[val] == 1:
                return ind
# to return the index of element that has only one occurrence in str s
        return -1