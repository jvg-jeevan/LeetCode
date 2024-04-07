class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        countof = 0
# check if the count of word is same then increment the result
        for i in words1:
            if (words1.count(i) == 1) and (words2.count(i) == 1):
                countof += 1
        return countof