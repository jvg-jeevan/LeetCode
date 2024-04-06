class Solution:
    def maximum69Number (self, num: int) -> int:
# convert the number to list and assign the number as high
        high = num
        num = list(map(int, str(num)))
# convert the 9 to 6 at first occurrence and break
        for i in range(len(num)):
            if num[i] == 6:
                num[i] = 9
                break
# convert the list to integer and compare if a greater than num return a
        a = int(''.join(list(map(str, num))))
        if a > high:
            return a
        return high
# if no greater element then return num