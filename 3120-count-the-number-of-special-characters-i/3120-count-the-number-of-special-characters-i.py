class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
# initialize res to store the count 
        res = 0
# convert the str word to char set and iterate through each char
        for char in set(word):
# check if both upper and lower exist and increment res
            if (char.upper() in word) and (char.lower() in word):
                res += 1
# return res/2 because it counts for caps and small twice
        return res // 2

# # create two sets for storing small and caps letters
#         small = set()
#         caps = set()
# # iterate through each char to find and add to caps or small
#         for char in word:
#             if char.islower():
#                 small.add(char)
#             else:
#                 caps.add(char)
# # initialize res to store the result count
#         res = 0
# # for each char in caps convert to lower and check of existance if True increment res
#         for i in caps:
#             if i.lower() in small:
#                 res += 1
#         return res