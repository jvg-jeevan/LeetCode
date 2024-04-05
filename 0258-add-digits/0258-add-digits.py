class Solution:
    def addDigits(self, num: int) -> int:
        # # conver the number to string and then list of integers
        # res = sum(list(map(int, str(num))))
        # # if the result is greater than 9 then call the function recursively
        # if res > 9:
        #     return self.addDigits(res)
        # # else return the result
        # return res

        if n == 0:
            return 0
        if n%9 == 0:
            return 9
        else:
            return n%9