class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # ans = 0
        # for i in range(n):
        #     ans ^= start
        #     start += 2
        # return ans

# create a list with values  nums[i] = start + 2 * i
        nums = [start + 2*i for i in range(n)]

# xor operation of number with zero results in number and then xor each element and return result
        ans = 0
        for x in nums:
            ans ^= x
        return ans