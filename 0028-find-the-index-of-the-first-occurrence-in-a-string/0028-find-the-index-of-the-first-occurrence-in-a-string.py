class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
            # if not found return -1 else return the first indexs
        else:
            return haystack.index(needle)