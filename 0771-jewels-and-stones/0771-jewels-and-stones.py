class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
#initialize res 
        res = 0
# for each char in stones if it is in jewels increment res
        for i in stones:
            if i in jewels:
                res += 1
        return res
# return the res