class Solution:
    def isFascinating(self, n: int) -> bool:
# multipl the number with 1, 2, 3 and convert to string and sorted() converts the string to the list in sorted order
        num = sorted(str(n) + str(n*2) + str(n*3))
        return num == ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# return True if it contains all the numbers