class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
# convert the str s to list
        string = s.split()
# if length of list string is not equal to number of char in pattern the False
        if len(string) != len(pattern):
            return False
# create a dictionary, key = char in pattern, value = element in list
        dict1 = {}
        for i in range(len(string)):
            dict1[pattern[i]] = string[i]
# this maps the pattern to the s

# if the dict contains any duplicate values return False
        if len(dict1.values()) != len(set(dict1.values())):
            return False

# if the value for dictionay is not equal to the string element then False, for each element in pattern and string run a loop and get the value for the pattern that should match with string element
        for x, y in zip(pattern, string):
            if dict1[x] != y:
                return False
        return True              