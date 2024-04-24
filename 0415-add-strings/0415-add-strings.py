class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
# change the limit
        sys.set_int_max_str_digits(10000)
# converting str to int using dict() for each key get the value and multiply num by 10 and the value
        values = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '0': 0}
        number1 = 0
        for x in num1:
            number1 = (number1 * 10) + values[x]


# converting str to int using ord() by getting unicode value of each digit (from 48 to 58) and subtracting it with ord('0') -> 48 gives the number
        number2 = 0
# for each digit after converting to int, multiply num with 10 and add the digit
        for y in num2:
            number2 = (number2 * 10) + (ord(y) - ord('0'))

# get the sum and then return the str() of this
        return str(number1 + number2)