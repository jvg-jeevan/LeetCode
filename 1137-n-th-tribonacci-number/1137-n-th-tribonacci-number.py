class Solution:
    def tribonacci(self, n: int) -> int:
# similar to fibonacci t0= 0, t1= 1, t2= 1 and t3= t1+t2+t3
        if n == 0:
            return 0
        elif n < 3:
            return 1
        else:
            n1, n2, n3 = 0, 1, 1
            for i in range(3, n+1):
                temp = n1 + n2 + n3
                n1, n2, n3 = n2, n3, temp
            return temp
# return nth tribonacci