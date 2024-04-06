class Solution:
    def numberOfSteps(self, num: int) -> int:
# number = 0 steps = 0
        if num == 0:
            return 0
# intitalize step
        step = 0
# while num > 0
        while num:
        # if num is odd then it needs 2 step i.e subtract 1 and divide by 2
            if num & 1:
                step += 2
        # if number is even then 1 step to divide by 2 
            else:
                step += 1
        # divide the number by 2 (right shift)
            num >>= 1
# return step - 1 as num becomes 1 even though its odd it only takes 1 step
        return step - 1