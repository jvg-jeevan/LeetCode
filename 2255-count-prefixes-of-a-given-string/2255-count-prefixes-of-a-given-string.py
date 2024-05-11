class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:

# approach 1
# res to store the count of elements
        res = 0
# for each word in words
        for word in words:
# if word is prefix of s then increment res
            if s.startswith(word):
                res += 1
# return the res
        return res

# # approach 2
# # count to store result
#         count = 0
# # for each word in words
#         for word in words:
# # if substring of s[to lenof word] is equal to word increment count
#             if s[0:len(word)] == word:
#                 count+=1
#         return count