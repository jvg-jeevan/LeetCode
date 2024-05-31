class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
# if length of matrix is less than 2 then return the list as it is
        if len(nums) <= 1:
            return nums
# mid is the middle index of the array nums
        mid = len(nums)//2
# divide the array into two parts
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
# call the function merge_sort() for both left and right part
        return self.merge_sort(left, right)


    def merge_sort(self, left, right):
        """method returns merged sorted list of elements"""
# initialize res to store the sorted and merged elements
        res = []
# l and r are index to traverse through the element
        l = r = 0
# continue in until both of l and r are less than lengths
        while l < len(left) and r < len(right):
# if left is greater than right the append left to res and increment l
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
# if right is greater than left then append right and increment r
            else:
                res.append(right[r])
                r += 1
# add the remaining element to res from both left and right
        res.extend(left[l:])
        res.extend(right[r:])

# return the resultant list
        return res