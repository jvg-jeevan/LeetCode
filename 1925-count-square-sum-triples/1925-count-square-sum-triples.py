class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
# a in range(n) and b in range(a)
        for a in range(1, n):
            for b in range(1, a):
# if integer part of c is equal to c then its perfect sqrt and also c should be less than n
                c = (a**2 + b**2) ** 0.5
                # the condition
                if int(c) == c and c <= n:
                    res += 2
# res + 2 because of the combinations (3, 4, 5) and (4, 3, 5)
        return res