from collections import *

class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:

        players = set()
        loss_count = defaultdict(int)


        for win, loss in matches:
            players.add(win)
            players.add(loss)
            loss_count[loss] += 1

        print(players)
        print(loss_count)

        not_lost = [person for person in players if loss_count[person] == 0]

        one_lost = [person for person in players if loss_count[person] == 1]

        return [sorted(not_lost), sorted(one_lost)]