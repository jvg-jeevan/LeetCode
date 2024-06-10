class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        
        res = 0
        for he, ex in zip(heights, expected):
            if he != ex:
                res += 1
            
        return res