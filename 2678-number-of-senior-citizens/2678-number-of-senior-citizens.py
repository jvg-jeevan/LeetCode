class Solution:
    def countSeniors(self, details: List[str]) -> int:
# res to store the number of passangers
        res = 0
# for each passanger
        for num in details:
# num[11:13] gives the age of passanger is strictly greater than 60 increment res
            if int(num[11:13]) > 60:
                res += 1
# return the number of passangers greater than age 60
        return res