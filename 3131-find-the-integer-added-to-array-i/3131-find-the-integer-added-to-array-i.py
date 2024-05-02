class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
#         nums1.sort()
#         nums2.sort()
# # sort the elements in the list and get difference of 1st elements
#         return nums2[0] - nums1[0]

        return min(nums2) - min(nums1)
# as the integer to be added will be same so get the difference of the minimum elements