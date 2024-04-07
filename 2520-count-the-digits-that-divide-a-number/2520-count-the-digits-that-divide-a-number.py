class Solution:
    def countDigits(self, num: int) -> int:
# result stores the number of digits that can divide the num
        result = 0
        temp = num
    # copy the num to temp variable
        while num:
            # get every digit
            rem = num % 10
            # check if it can divide the num
            if rem != 0 and temp % rem == 0:
                result+=1
                # if yes increment the result
            num //= 10
        return result