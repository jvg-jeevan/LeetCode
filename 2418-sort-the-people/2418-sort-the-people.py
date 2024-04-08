class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
# students stores height of each student key = heights, value= names (because names has duplicates)
        students = {}
# zip() is used to take one element at a time from both the list
        for x, y in zip(names, heights):
            students[y] = x
# to sort the heights in decreasing order i.e students.items() gets the tuple(key, value) so sorting based on key(heights) so inside lambda item[0] and reverse = True
        students = dict(sorted(students.items(), key= lambda item: item[0], reverse= True))
        # after sorting return the values in dict(students) i.e names
        return list(students.values())