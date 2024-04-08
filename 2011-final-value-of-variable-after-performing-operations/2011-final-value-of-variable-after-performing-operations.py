class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

# # approach 1
#         res = 0
# # initialize res
#         for char in operations:
#         # if decrement then -1
#             if char in ['--X', 'X--']:
#                 res -= 1
#         # if increment then +1
#             else:
#                 res += 1
#         return res

        X = 0
        # initialize X
        for char in operations:
        # if + is found in each operation increment
            if '+' in char:
                X += 1
        # if not + or - decrement
            else:
                X -= 1
        return X