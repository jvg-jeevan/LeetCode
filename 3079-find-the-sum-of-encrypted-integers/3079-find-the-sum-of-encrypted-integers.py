class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
# nums list containing the str() of nums int() list
        nums = list(map(str, nums))
        sumof = 0
# if number is (123) the max digit in number is 3 so encrypted num becomes 333
        for i in nums:
            sumof += int(max(i) * len(i))
        # get the encrypted num and add that to sum and return sumof
        return sumof