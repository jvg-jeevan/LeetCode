class Solution:
    def heightChecker(self, heights: List[int]) -> int:
# expected is the new sorted array
        expected = sorted(heights)
# res to store the count of the numbers not equal
        res = 0
# take 1 element from each element from heights and expected
        for he, ex in zip(heights, expected):
# if element at position are not equal then increment res 
            if he != ex:
                res += 1
# return the result res
        return res