# import re

# class Solution:
#     def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
#         paragraph = (re.sub(r'[^a-zA-Z0-9\s]', '', paragraph)).lower()
#         for i in range(len(banned)):
#             paragraph = paragraph.replace(banned[i], '')
#         paragraph = paragraph.split()

#         dict1 = {}
#         for i in paragraph:
#             dict1[i] = paragraph.count(i)

#         maxi = max(dict1.values())
#         for x, y in dict1.items():
#             if y == maxi:
#                 return x

import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Remove special characters and convert to lowercase
        paragraph = re.sub(r'[^a-zA-Z0-9\s]', ' ', paragraph).lower()
        
        # Split paragraph into words and filter out banned words
        words = [word for word in paragraph.split() if word not in banned]

# key = word and value = count 
        freq = {}
        for x in set(words):
            freq[x] = words.count(x)

# get the key with maximum value and return the key
        maxi = max(freq.values())
        for key, val in freq.items():
            if val == maxi:
                return key

        # # Count word frequencies using Counter
        # word_counts = Counter(words)
        
        # # Find the most common word
        # return max(word_counts, key=word_counts.get)
