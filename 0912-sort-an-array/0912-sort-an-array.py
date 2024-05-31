class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
            
        mid = len(nums)//2

        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge_sort(left, right)



    def merge_sort(self, left, right):
        res = []
        l = r = 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                res.append(left[l])
                l += 1
            else:
                res.append(right[r])
                r += 1

        res.extend(left[l:])
        res.extend(right[r:])
        return res