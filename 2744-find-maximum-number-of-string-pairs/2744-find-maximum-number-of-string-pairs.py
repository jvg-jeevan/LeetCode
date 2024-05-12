from collections import Counter
class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        res = Counter(tuple(sorted(each)) for each in words)
        ans = 0
        for key, val in res.items():
            if val == 2:
                ans += 1
        return ans