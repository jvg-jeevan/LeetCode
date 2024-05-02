class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
# create two sets to store unique and duplicate elemetns
        uni = set() 
        dup = set()
        for i in nums:
            if i in uni:
                dup.add(i)
            else:
                uni.add(i)
# return the dup set
        return dup