class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
# if length of
        if len(set(sorted(s))) != len(set(sorted(t))):
            return False
        dict1 = {}
        for i in range(len(t)):
            dict1[t[i]] = s[i]

        for x in range(len(s)):
            if s[x] != dict1[t[x]]:
                return False
        return True