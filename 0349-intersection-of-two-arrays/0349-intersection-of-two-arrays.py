class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
# convert the lists to set and then use & (intersect) to find the intersection and then return the list

# list(set(nums1).intersect(set(nums2)))