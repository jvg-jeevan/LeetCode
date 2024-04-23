class Solution:
    def largestOddNumber(self, num: str) -> str:
# get the length of the num - 1 (because 0 indexing)
        i = len(num) - 1
# go through the num from rightmost end and check if even then continue if odd break out of loop 
        while (i >= 0) and (int(num[i]) % 2 == 0):
            i -= 1
# if any digit in num is odd then return the num until that digit
        return num[:i+1] if i >=0 else ''
# if no digits found then return ''



# # if num is odd then return the number
#         if int(num) % 2 != 0:
#             return num
# # iterate throught the num from last
#         for i in range(len(num)-1,-1, -1):
# # if the digit of that num is odd then return the string upto including that digit in nums
#             if int(num[i]) % 2 != 0:
#                 return num[:i+1]
#         return ""  # If no odd digits are found, return an empty string