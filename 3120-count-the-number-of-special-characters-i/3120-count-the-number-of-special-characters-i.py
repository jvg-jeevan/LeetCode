class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
# create two sets for storing small and caps letters
        small = set()
        caps = set()
# iterate through each char to find and add to caps or small
        for char in word:
            if char.islower():
                small.add(char)
            else:
                caps.add(char)
# initialize res to store the result count
        res = 0
# for each char in caps convert to lower and check of existance if True increment res
        for i in caps:
            if i.lower() in small:
                res += 1
        return res