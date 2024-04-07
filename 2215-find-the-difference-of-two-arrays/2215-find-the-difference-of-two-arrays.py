class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
# first approach is finding elements not in each list add to result and return
        # out_list = [[], []]
        # for i in set(nums1):
        #     if i not in nums2:
        #         out_list[0].append(i)
        # for j in set(nums2):
        #     if j not in nums1:
        #         out_list[1].append(j)
        # return out_list

# finding set differences of each set and returnt the result
        return [set(nums1) - set(nums2), set(nums2) - set(nums1)]