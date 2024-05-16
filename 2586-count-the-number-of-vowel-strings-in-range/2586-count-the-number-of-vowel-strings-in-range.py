class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
# create a list of vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
# initialize res to 0 store the count
        res = 0
# iterate through each word in words[left to right inclusive] 
        for word in words[left: right+1]:
# if 1st and last char in word is in vowels list then increment res
            if (word[0] in vowels) and (word[-1] in vowels):
                res += 1
# return the res count
        return res