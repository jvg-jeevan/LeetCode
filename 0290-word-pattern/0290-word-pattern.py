class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        string = s.split()
        if len(string) != len(pattern):
            return False
        dict1 = {}
        for i in range(len(string)):
            dict1[pattern[i]] = string[i]

        if len(dict1.values()) != len(set(dict1.values())):
            return False

        for x, y in zip(pattern, string):
            if dict1[x] != y:
                return False
        return True              