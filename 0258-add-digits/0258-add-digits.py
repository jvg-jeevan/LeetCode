class Solution:
    def addDigits(self, num: int) -> int:
        # using recursion
        # # conver the number to string and then list of integers
        # res = sum(list(map(int, str(num))))
        # # if the result is greater than 9 then call the function recursively
        # if res > 9:
        #     return self.addDigits(res)
        # # else return the result
        # return res

# if num is completely divisible by 9 then sum will be 9
# else sum will be the remainder
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9