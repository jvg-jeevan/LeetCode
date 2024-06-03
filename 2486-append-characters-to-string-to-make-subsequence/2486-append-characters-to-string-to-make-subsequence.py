class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
# initialize pointers j and j
        i = j = 0

# to check for subsequence take continuous numbers
# iteratre until both i and j are less than len(s) and len(t)
        while i < len(s) and j < len(t):
# if chars are equal then increment j
            if s[i] == t[j]:
                j += 1
# increment the i to check for next char
            i += 1

        return len(t) - j