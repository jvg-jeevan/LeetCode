class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
# define a function to find whether the nymber divides itself
        def is_self(num):
        # if digit is zero or not completely return False
            for digit in str(num):
                if (digit == '0') or (num % int(digit) != 0):
                    return False
            return True

        # result = []
        # for num in range(left, right+1):
        #     if is_self(num):
        #         result.append(num)
        # return result
        return [num for num in range(left, right+1) if is_self(num)]
# for loop in range(left and right) is result of is_self() is true add the numebr to list and return result