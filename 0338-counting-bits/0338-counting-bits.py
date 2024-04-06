class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
# for each number in range convert to binary and then to string and then count the number of 1s and append that to list
        for i in range(n+1):
            res.append(str(bin(i)).count('1'))
        return res