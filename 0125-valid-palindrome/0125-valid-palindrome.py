class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # convert the string to lowercase
        s = ''.join(x for x in s if x.isalnum())
        # join only alphabets 
        return s == s[::-1]
        # if string s == reverse s return True