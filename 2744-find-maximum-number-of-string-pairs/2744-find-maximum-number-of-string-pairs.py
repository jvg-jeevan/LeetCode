from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
# res dict() key = tuple(sorted elements(list)) and value = occurrences (pairs)
        res = Counter(tuple(sorted(each)) for each in words)
# ans to store the occurrences
        ans = 0
# check if pairs increment pairs
        for key, val in res.items():
            if val == 2:
                ans += 1
# return the number of pairs
        return ans