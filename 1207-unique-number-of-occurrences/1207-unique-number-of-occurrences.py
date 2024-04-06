class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
# res list contains the count of the occurrences of element in the list
        res = []
        for i in set(arr):
            i = arr.count(i)
# if the count of element is already in list return False
            if i in res:
                return False
            else:
                res.append(i)
        return True
# if all the occurrences are unique then return True