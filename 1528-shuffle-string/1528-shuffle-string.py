class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dict1 = {}
        s2 = ''
# dict1 mapping of each letter to index , key= index, value= character
        for i in range(len(s)):
            dict1[indices[i]] = s[i]
# sort the keys in dict1 and it returns list of sorted keys dict2
        dict2 = sorted(dict1)

# for each key index in dict2 get the value for key in dict1
        for i in dict2:
            s2 += dict1[i]
# append the value to the string
        return s2