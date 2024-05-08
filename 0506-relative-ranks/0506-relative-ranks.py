class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
# sort the scores in reverse order and assign to ranks
        ranks = sorted(set(score), reverse=True)

# positions is dict() to store rank i.e gold, silver, bronze or other
        positions = {}
# ind -> index val -> values
        for ind, val in enumerate(ranks):
            if ind == 0:
                positions[val] = 'Gold Medal'
            elif ind == 1:
                positions[val] = 'Silver Medal'
            elif ind == 2:
                positions[val] = 'Bronze Medal'
            else:
                positions[val] = str(ind+1)

# return the list with ranks to score with relative positions
        return [positions[i] for i in score]