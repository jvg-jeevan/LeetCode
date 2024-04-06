class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0:
            return 0
        step = 0
        while num:
            if num & 1:
                step += 2
            else:
                step += 1
            num >>= 1
        return step - 1
# class Solution:
#     def numberOfSteps(self, num: int) -> int:
#         step = 0
#         while num:
#             if num & 1:  # Check if num is odd
#                 step += 2  # Increment step by 2 for the two operations
#             else:
#                 step += 1  # Increment step by 1 for division by 2
#             num >>= 1  # Right shift num by 1 bit (equivalent to num //= 2)
#         return step - 1  # Subtract 1 to account for the extra step when num becomes 0
