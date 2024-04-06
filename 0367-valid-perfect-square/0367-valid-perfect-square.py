class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        root = int(num ** 0.5)
        return num == (root ** 2)
# if the integer part of root is equal to the square of root the its a valid square