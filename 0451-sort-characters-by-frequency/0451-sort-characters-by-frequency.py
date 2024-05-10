from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        res = sorted(s)
        res = Counter(res)
        ans = ''

        res = dict(sorted(res.items(), key= lambda items: items[1], reverse= True))

        for key, val in res.items():
            ans += val * key
            
        return ans