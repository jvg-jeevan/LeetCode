class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
# sort the list nums
        nums.sort()
# initialize result
        result = 0
# for each element if less than k increment result, if element is greater break out of loop
        for i in nums:
            if i < k:
                result += 1
            elif i >= k:
                break
        return result