from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
# if the concatenation of both string is not equal then return ' '
        if (str1 + str2) != (str2 + str1):
            return ''
# get the length of both the strings
        s1 = len(str1)
        s2 = len(str2)
# return the substring until gcd
        return str2[:gcd(s1, s2)]


# # finding the gcd of the length using Euclidean algorithm
#         while s2 != 0:
#             s1, s2 = s2, s1 % s2
# # return the substring of str2 upto length of gcd
#         return str2[:s1]