class Solution:
    def kthSmallestPrimeFraction(self, arr: list[int], k: int) -> list[int]:
# res to store the pairs
        res = []
# iterate through each element in i and j loops
        for i in range(len(arr)-1):
            for j in range(i+1, len(arr)):
# append the pairs to res
                res.append([arr[i], arr[j]])
        
# sort the pairs based on the division of pairs
        res.sort(key= lambda item: item[0]/item[1])

# return the kth pair in the res
        return res[k-1]