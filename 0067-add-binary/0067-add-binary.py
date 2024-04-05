class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        # reverse the string to get decimal of the binary number because string indexing start from right 0
        b = b[::-1]
        # initialize numbers 
        num1, num2 = 0, 0

        # convert to binary by multiplying each to 2 powers 
        for i in range(len(a)):
            rem = int(a[i]) * (2**i)
            num1 += rem

        for j in range(len(b)):
            rem = int(b[j]) * (2**j)
            num2 += rem
        
        # add two numbers and convert to binary and return excluding '0b' part
        s1 = str(bin(num1 + num2))
        return s1[2:]