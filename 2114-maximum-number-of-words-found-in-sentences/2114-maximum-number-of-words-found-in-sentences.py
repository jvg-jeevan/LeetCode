class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(words.split()) for words in sentences)
        # split() each sentence and get the length of the same and get max value from that