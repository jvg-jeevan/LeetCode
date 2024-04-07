class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # rich = 0
        # for i in accounts:
        #     rich = max(rich, sum(i))
        # return rich
# get the sum of each list and get the maximum sum of all lists
        return max(sum(person) for person in accounts)