class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            n1, n2 = 0, 1
            for i in range(2, n+1):
                n3 = n1+n2
                n1, n2 = n2, n3
            return n3
# if n=0 fib(0) = 0 if n=1 fib(1) = 1
# if n >= 2 then fib logic and return the fib of nth number