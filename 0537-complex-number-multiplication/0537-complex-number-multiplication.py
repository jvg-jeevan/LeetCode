class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
# split the numbers into list at '+'
        num1 = num1.split('+')
        num2 = num2.split("+")

# get the a, c real part 
        a, c = int(num1[0]), int(num2[0])
# b, d imaginary part excluding i
        b, d = int(num1[1][:-1]), int(num2[1][:-1])

# formula for multiplication (a+ib) * (c+id) = (ac - bd) + (ad + bc)i

# calculate the values according to formula
        real = str(a*c - b*d)
        imag = str(a*d + b*c)

# return the result in complex number format
        return real + '+' + imag + 'i'