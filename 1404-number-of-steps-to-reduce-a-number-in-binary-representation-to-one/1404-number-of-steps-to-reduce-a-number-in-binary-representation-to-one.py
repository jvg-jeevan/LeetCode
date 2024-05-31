class Solution:
    def numSteps(self, s: str) -> int:
        num = 0
        s = list(map(int, s))[::-1]
        print(s)

        for ind, (val) in enumerate(s):
            num += (val * (2 ** ind))
        print(num)

         
        res = 0
        while num > 1:
            if num == 1:
                break
            elif num % 2 == 0:
                num >>= 1
                res += 1
            else:
                num += 1
                res += 1
            
            
        return res