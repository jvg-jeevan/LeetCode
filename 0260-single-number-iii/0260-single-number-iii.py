class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

# approach 1
# get the occurrences of the elements in nums if count is 1 then append to the result list
        # return [i for i in set(nums) if nums.count(i) == 1]

# approach 2
# res is set()
        res = set()
# for every element in nums
        for i in nums:
# if i is in res remove the element
            if i in res:
                res.remove(i)
# if i not in set then add i
            else:
                res.add(i)
# return res 
        return res