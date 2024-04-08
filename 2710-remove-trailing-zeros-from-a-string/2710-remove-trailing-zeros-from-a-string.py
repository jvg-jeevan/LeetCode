class Solution:
    def removeTrailingZeros(self, num: str) -> str:
# reverse the string and then convert to int (removes trailing zeros) and then convert to string and return the reverse of number
        return str(int(num[::-1]))[::-1]