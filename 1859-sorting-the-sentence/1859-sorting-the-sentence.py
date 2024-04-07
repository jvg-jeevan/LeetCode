class Solution:
    def sortSentence(self, s: str) -> str:
# split the string to list
        arr = s.split()
# dict1{} stores the order of occurrences of string and also the string
# key= the rank at last of string, value= the string
        dict1 = {}
        for word in arr:
            dict1[int(word[-1])] = word[0:-1]
# result string holds the words placed in order according to the ranks
        result = [dict1[i] for i in range(1, len(arr)+1)]
# return the result by adding the elements to string
        return ' '.join(result)