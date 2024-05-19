class Solution:
    def splitNum(self, num: int) -> int:
# nums stores the sorted string value
        nums = sorted(str(num))
# even contains digits in even index
        even = ''
# odd contains digits in odd index
        odd = ''
# add the digits to even and odd for index
        for i in range(len(nums)):
            if i % 2 == 0:
                even += nums[i]
            else:
                odd += nums[i]

# return the sum of integer part of even and odd
        return int(even) + int(odd)