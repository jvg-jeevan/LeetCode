class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
# check if any number exists in both the lists
        nums3 = [i for i in nums1 if i in nums2]
# if any element exists in nums3 then return the minimum element
        if nums3:
            return min(nums3)
        
# n1 and n2 stores the minimum element of both the lists nums1 and nums2
        n1 = min(nums1)
        n2 = min(nums2)

# check which of n1 and n2 is greater then return the number with lesser digit to the left and the other digit 
        if n1 < n2:
            return int(str(n1) + str(n2))
        else:
            return int(str(n2) + str(n1))
