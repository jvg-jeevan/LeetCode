class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
# approach 1
        # s[:] = s[::-1]
# s[:] is used to modify the list in place instead of craeting a new instance

# approach 2
# initialize left as 0 and right as last element index
        left = 0
        right = len(s) - 1
# iterate until left index is less than right
        while left < right:
# swap the left and right element
            s[left], s[right] = s[right], s[left]
# increment left and decrement right
            left += 1
            right -= 1