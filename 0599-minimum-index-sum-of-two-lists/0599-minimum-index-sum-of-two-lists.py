class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
# get the elements in both the list
        out_list = [x for x in list1 if x in list2]
# if only one element is common then return the element
        if len(out_list) == 1:
            return out_list

# dict1 is used to store the sum of indexes of common elements 
        dict1 = {}
# key= word, value= sum of index of word
        for word in out_list:
            dict1[word] = list1.index(word) + list2.index(word)

# return the elements which has the minimum sum
        return [i for i, j in dict1.items() if j == min(dict1.values())]
# comparing the values to minimum value get the key