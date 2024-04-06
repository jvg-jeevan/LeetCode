class Solution:
    def checkRecord(self, s: str) -> bool:
# convert the string to list
        stud = list(map(str, s))
# if the count of 'A' i.e absent > 1 then False
        if stud.count('A') > 1:
            return False
# this is to check the condition that 3 leaves are in a row then return False
        for i in range(1, len(stud) - 1):
            if stud[i] == 'L' and stud[i-1] == 'L' and stud[i+1] == 'L':
                return False
        return True