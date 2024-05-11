class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
# res to store the count of elements
        res = 0
# for each word in words
        for word in words:
# if word is prefix of s then increment res
            if s.startswith(word):
                res += 1
# return the res
        return res