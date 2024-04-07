class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict1 = {}
        s2 = ''
        for i in range(len(s)):
            dict1[indices[i]] = s[i]
        dict2 = sorted(dict1)
        for i in dict2:
            s2 += dict1[i]
        return s2 