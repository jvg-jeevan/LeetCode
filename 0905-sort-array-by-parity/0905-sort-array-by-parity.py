class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
# get the even and odd numbers in lists and return even and odd lists
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd