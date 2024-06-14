class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = [i for i in nums1 if i in nums2]

        if nums3:
            return min(nums3)
        

        n1 = min(nums1)
        n2 = min(nums2)

        if n1 < n2:
            return int(str(n1) + str(n2))
        else:
            return int(str(n2) + str(n1))
