class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    # pop() the last element out and insert that at index 0
        for i in range(k):
            nums.insert(0, nums.pop())