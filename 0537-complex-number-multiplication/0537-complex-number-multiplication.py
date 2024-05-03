class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
# split the numbers into list at '+'
        num1 = num1.split('+')
        num2 = num2.split("+")

# formula for multiplication (a+ib) * (c+id) = (ac - bd) + (ad + bc)i

# get the a, c real part and b, d imaginary part
        a, c = int(num1[0]), int(num2[0])
        b, d = int(num1[1][:-1]), int(num2[1][:-1])

# calculate the values according to formula
        real = str(a*c - b*d)
        imag = str(a*d + b*c)

# return the result in complex number format
        return real + '+' + imag + 'i'