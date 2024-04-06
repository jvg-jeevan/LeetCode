class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
# dict1 to store the occurrences of elements in arr1
        dict1 = {}
        res = []
# rem contains sorted remaining elements that are not in arr2
        rem = sorted([x for x in arr1 if x not in arr2])
# count the elements of srr1 and store in dict1
        for i in arr2:
            dict1[i] = arr1.count(i)
# create a list for every key and value i.e sort in the order of arr2
        for x, y in dict1.items():
            temp = [x] * y
            res.extend(temp)
# add the rem elements to res and return result
        res.extend(rem)
        return res