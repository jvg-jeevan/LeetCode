class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
# word3 contains result
        word3 = ''
# this is to make the length of string equal
# add the whitespaces to the word that has less characters than the other
# ljust is used to add desired character at the end of string upto specified number of spaces
        if len(word1) <= len(word2):
            word1 = word1.ljust(max(len(word1), len(word2)))
        else:
            word2 = word2.ljust(max(len(word1), len(word2)))

# for each character in word1 and word2 if char is whitespace then add only other words character of else add the characters alternately
        for i in range(len(word1)):
            if word1[i] == ' ':
                word3 += word2[i]
            elif word2[i] == ' ':
                word3 += word1[i]
            else:
                word3 += (word1[i] + word2[i])
        return word3