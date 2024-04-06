class Solution:
    def reverseWords(self, s: str) -> str:
# convert the string to list
        s = s.split()
# new_string will store the reverse of each word
        new_string = [i[::-1] for i in s]
# join the reversed words and return the result
        return ' '.join(new_string)