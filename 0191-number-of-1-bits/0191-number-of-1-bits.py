class Solution:
    def hammingWeight(self, n: int) -> int:
        # return str(bin(n)).count('1')
        # converting the number to binary and then to string and count digits with one

# when number is greater than 0, convert to binary i.e divide by 2
        res = 0
        while n > 0:
            # if remainder is not zero then increment res
            if n%2 != 0:
                res += 1
            # get the remaining number
            n //= 2
        return res