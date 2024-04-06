class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
# res dict() contains number of 1's in each row of mat
# key = index of row in matrix, value = no. of 1's
        res = {}
        for i in range(len(mat)):
            res[i] = mat[i].count(1)

# sorting the dict(res) based on values
# res.items() returns a tuple (key, value) in lambda item[1] means value
        res = dict(sorted(res.items(), key=lambda item: item[1]))
# out contains keys for sorted values
        out = list(res.keys())
# return the rank until k
        return out[:k]