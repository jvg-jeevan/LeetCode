class Solution:
    def search(self, nums: List[int], target: int) -> int:
# the index at which the array is rotated i.e the elements previous to that is greater
        if target in nums:
            # if target found return index else return -1
            return nums.index(target)
        return -1