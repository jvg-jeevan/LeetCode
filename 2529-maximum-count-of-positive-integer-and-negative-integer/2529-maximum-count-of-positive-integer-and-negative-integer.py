class Solution:
    def maximumCount(self, nums: List[int]) -> int:
# pos, neg to store the number of pos and neg numbers
        pos = 0
        neg = 0
# iterate through each element in nums if +ve increment pos, if -ve increment neg
        for num in nums:
            if num > 0:
                pos += 1
            elif num < 0:
                neg += 1
# return the maximum among pos and neg count
        return max(pos, neg)