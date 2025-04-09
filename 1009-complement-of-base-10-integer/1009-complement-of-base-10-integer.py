class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # convert to binary removing '0b'
        num = bin(n)[2:]
        # reverse 1's and 0's and join the string
        comp_num = ''.join(['1' if i == '0' else '0' for i in num])
        # return the int part with base 2
        return int(comp_num, 2)