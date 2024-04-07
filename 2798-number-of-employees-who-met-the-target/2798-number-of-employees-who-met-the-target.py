class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
# initialize the result
        result = 0
    # for each element is greater than target increment the result
        for i in hours:
            if i >= target:
                result += 1
        return result