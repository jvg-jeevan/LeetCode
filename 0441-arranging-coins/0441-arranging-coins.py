class Solution:
    def arrangeCoins(self, n: int) -> int:
# i= number of coins placed
        i = 1
# arranging the coins from 1 
        while n >= i:
            n -= i
            i += 1
        return i - 1
# while number of coins is greater than the number of coins placed
# decrement n, i.e n will be remaining coins
# increment i, i.e wiil be the rows placed