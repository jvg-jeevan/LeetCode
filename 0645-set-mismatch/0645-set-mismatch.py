class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # ele = 0
        # dou = 0 
        # for i in range(1, n+1):
        #     if i not in nums:
        #         ele = i
        
        # for x in set(nums):
        #     if nums.count(x) > 1:
        #         dou = x
        
        # return [dou, ele]

        # n = len(nums)
        # dou = 0 
        # sum1 = (n*(n+1))//2
        # for x in set(nums):
        #     if nums.count(x) > 1:
        #         dou = x
        # ele = sum1 - sum(nums) + dou
        # return [dou, ele]

        n = len(nums)
        dup = -1
# initialize the dup element as -1
        sum1 = (n*(n+1))//2
# sum1 will the actual sum of the elements
        seen = set()
# seen will be the visited elements 
        for i in nums:
            if i in seen:
                dup = i
            else:
                seen.add(i)
# get the dup element and also the missing number and return the dup and missing number
        miss = sum1 - sum(seen)
        return [dup, miss]