class Solution:
    def longestPalindrome(self, s: str) -> int:
        # res to store the number of letters in palindrome
        res = 0
        # letters is set to store the chars to be in palindrome
        letters = set()

        # iterate through each char in s
        for i in s:
            # if char is already in set letters then remove the letter and increment res by 2 (i.e element is occurring again or 2 times)
            if i in letters:
                letters.remove(i)
                res += 2
            # if element not in letters then add char to letters
            else:
                letters.add(i)

        # if any element is left in the letters set then increment res by 1 i.e center element can only be one element if not two element
        if letters:
            res += 1
# return the res or length of palindrome
        return res