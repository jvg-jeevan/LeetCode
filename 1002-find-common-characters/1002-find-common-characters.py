from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:

# letters_count holds the count of the letters and store in dict at indexes same as the words
        letters_count = [Counter(word) for word in words]

# initail will store the first element from letters_count
        initail = letters_count[0]

# take each element from letters_count and do the intersection of dictionaries i.e like intersection of sets that takes the tuple (items)
        for i in range(1, len(letters_count)):
            initail &= letters_count[i]

# res to store the letters with number of occurrences
        res = ''
        for key, val in initail.items():
            res += val * key
            
# return the resultant string res
        return res