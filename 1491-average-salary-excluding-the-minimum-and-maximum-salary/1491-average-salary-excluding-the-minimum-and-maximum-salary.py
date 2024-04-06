class Solution:
    def average(self, salary: List[int]) -> float:
        # salary.sort()
        # salary.pop(0)
        # salary.pop(-1)
        # return sum(salary)/len(salary)

# to get the salary between greatest and smallest subtract sumof salary by minimum salary and maximum salary and find the avg by excluding the 2 salaries
        return (sum(salary) - min(salary) - max(salary)) / (len(salary)-2)