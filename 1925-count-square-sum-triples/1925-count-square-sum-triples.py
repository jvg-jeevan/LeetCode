class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, n):
            for b in range(1, a):
                c = (a**2 + b**2) ** 0.5
                if int(c) == c and c <= n:
                    res += 2
        return res