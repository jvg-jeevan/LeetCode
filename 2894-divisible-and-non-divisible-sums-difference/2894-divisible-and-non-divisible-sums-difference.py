class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
# create the list in range n
        list1 = list(range(1, n+1))
# initialize num1, num2
        num1, num2 = 0, 0
# for each number in list if divisble by m add num to num1 
# if not divisible add number to num2 
        for i in list1:
            if i % m != 0:
                num1 += i
            else:
                num2 += i
        return num1 - num2
    # return the difference between num1 - num2