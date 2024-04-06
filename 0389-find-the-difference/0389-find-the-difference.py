class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if t.count(i) != s.count(i):
                return i
# iterate through each element in t if the count of that element in t is not same as count in s then return that element