class Solution:
    def count_ones(self, num):
        """This function gets the number of ones in the binary representation of a number"""
        ones = 0
        while num != 0:
            if num % 2 != 0:
                ones += 1
            num //= 2
        return ones

    def countBits(self, n: int) -> List[int]:
        """This function gets the number of ones by calling the count_ones() function in the range of n"""
        return [self.count_ones(i) for i in range(n+1)]






#         res = []
# # for each number in range convert to binary and then to string and then count the number of 1s and append that to list
#         for i in range(n+1):
#             res.append(str(bin(i)).count('1'))
#         return res