class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
# get the occurrences of the elements in nums if count is 1 then append to the result list
        return [i for i in set(nums) if nums.count(i) == 1]