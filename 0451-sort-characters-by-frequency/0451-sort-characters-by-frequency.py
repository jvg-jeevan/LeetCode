from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
# sorted of the string input s results in sorted list of chars
        res = sorted(s)
# Counter() creates the dict(), key= char, value= number of occurrences
        res = Counter(res)

# sort the dict based on values
        res = dict(sorted(res.items(), key= lambda items: items[1], reverse= True))

# ans to store the result to return
        ans = ''

# iterate throught each item in dict add the number of chars to ans
        for key, val in res.items():
            ans += val * key
# return the result ans
        return ans