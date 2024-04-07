class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word3 = ''
        if len(word1) <= len(word2):
            word1 = word1.ljust(max(len(word1), len(word2)))
        else:
            word2 = word2.ljust(max(len(word1), len(word2)))
        for i in range(len(word1)):
            if word1[i] == ' ':
                word3 += word2[i]
            elif word2[i] == ' ':
                word3 += word1[i]
            else:
                word3 += (word1[i] + word2[i])
        return word3