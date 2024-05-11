class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
# split the sentence to list of words
        words = sentence.split()
# x is the lenght of searchWord
        x = len(searchWord)
# iterate through each element in words
        for ind, val in enumerate(words):
# if val starts with searchWord return the ind + 1 (as list is 0 indexed)
            if val[:x] == searchWord:
                return ind+1
# if no element found return -1
        return -1