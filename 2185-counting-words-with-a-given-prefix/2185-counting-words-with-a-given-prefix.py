class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
# res to store the count of elements
        res = 0
# for each word in list if starts with pref increment res
        for word in words:
            if word.startswith(pref):
                res += 1
# return the res
        return res