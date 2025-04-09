class Solution:
    def findComplement(self, num: int) -> int:
        # converting to binary eliminating '0b'
        bin_num = bin(num)[2:]
        # getting the complement of number
        comp_num = ''.join(['0' if i == '1' else '1' for i in bin_num])
        # converting the str to int of base 2
        return int(comp_num, 2)