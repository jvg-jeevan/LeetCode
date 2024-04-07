class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
# if length of s and t after removing duplicates are not same then False
        if len(set(sorted(s))) != len(set(sorted(t))):
            return False
# dict1 is used to map the chars in s and t, key = t, val = s
        dict1 = {}
        for i in range(len(t)):
            dict1[t[i]] = s[i]

# for every char in s if the mapped value in dict1 does not match then return False 
        for x in range(len(s)):
            if s[x] != dict1[t[x]]:
                return False
# if all the characters match in mapping then return True
        return True