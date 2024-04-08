class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
# initialize res
        for char in operations:
        # if decrement then -1
            if char in ['--X', 'X--']:
                res -= 1
        # if increment then +1
            else:
                res += 1
        return res