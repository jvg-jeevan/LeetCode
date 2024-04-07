class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
# iterate through each list inside list
        countof = 0
# check the condition given and if condition is True then increment countof and return result
        for i in range(len(items)):
            if ruleKey == 'type' and ruleValue == items[i][0]:
                countof += 1
            elif ruleKey == 'color' and ruleValue == items[i][1]:
                countof += 1
            elif ruleKey == 'name' and ruleValue == items[i][2]:
                countof += 1
        return countof