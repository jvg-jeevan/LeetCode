class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
# return the index of the string if x occurs in each element in list
        return [i for i in range(len(words)) if x in words[i]]