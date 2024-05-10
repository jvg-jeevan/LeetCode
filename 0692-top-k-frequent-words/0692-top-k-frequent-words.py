from collections import Counter

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
# count the occurrences of the elements in list usnig Counter()
        res = Counter(words)
# sort the dict based on the values
        res = dict(sorted(res.items(), key= lambda items: items[1], reverse=True))
# return the top k keys in res
        return list(res.keys())[:k]