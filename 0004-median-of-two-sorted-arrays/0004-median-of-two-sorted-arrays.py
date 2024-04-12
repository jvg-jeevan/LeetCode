class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # merge two lists
        arr = nums1 + nums2
        # sort() the list arr
        arr.sort()
        # n is length of arr
        n = len(arr)
        # if n is odd then middle element is the median
        if n%2 != 0:
            # to get the floor value of n/2 which becomes middle element
            ind = math.floor(n/2)
            # return the float of number at middle index 
            return float(arr[ind])
        # if len is even then take middle two elements
        else:
            # ind gets the middle element  
            ind = n//2
            # slice the arr middle elements i.e previous and next and get sum and avg of those
            return sum(arr[ind-1:ind+1])/2