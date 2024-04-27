from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# initialize dict() and value for this this dict() is empty list
        anagrams = defaultdict(list)

# iterate through each word in list
        for word in strs:
# sorted() returns a sorted list of chars and join() joins the chars to form str
            sorted_word = ''.join(sorted(word))
# for each word if the key matches or forms anagram then append to the values list
            anagrams[sorted_word].append(word)

# return the values list(list)
        return list(anagrams.values())