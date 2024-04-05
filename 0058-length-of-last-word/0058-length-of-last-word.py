class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[-1])
        # split() to the list and then take the last element in list and return the length of it