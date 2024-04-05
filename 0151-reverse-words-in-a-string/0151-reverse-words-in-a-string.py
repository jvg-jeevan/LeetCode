class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        # split the string to list 
        return ' '.join(list1[::-1])
        # reverse the list and join the list elements