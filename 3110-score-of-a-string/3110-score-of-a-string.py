class Solution:
    def scoreOfString(self, s: str) -> int:
# get the ascii values for each char
        values = [ord(i) for i in s]
# initialize res to 0 to store sum
        res = 0
# for each element get the abs difference of adjacent pairs and add to res
        for i in range(len(values)-1):
            res += abs(values[i] - values[i+1])

        return res