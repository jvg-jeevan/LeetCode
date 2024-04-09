class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
    # res to store the res
        res = 0
    # i and j loop to access every element
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                # n = to get element length
                n = len(words[i])
# if (prefix) words[j][:n] take the same length as the words[i] 
# if (suffix) words[j][-n:] (from the last nth element to last) take the same length as the words[i] 
                if words[i] == words[j][:n] and words[i] == words[j][-n:]:
                    res += 1
        return res