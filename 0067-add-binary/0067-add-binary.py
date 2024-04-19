class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]
        num1, num2 = 0, 0
        for i in range(len(a)):
            rem = int(a[i]) * (2**i)
            num1 += rem

        for j in range(len(b)):
            rem = int(b[j]) * (2**j)
            num2 += rem
        
        s1 = str(bin(num1 + num2))
        return s1[2:]