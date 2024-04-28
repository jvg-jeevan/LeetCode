class Solution:
    def countOdds(self, low: int, high: int) -> int:
# result contains even or odd numbres
        result = (high - low) // 2
# if any one of low or high is odd add 1 to result
        if (low % 2 != 0) or (high % 2 != 0):
            result += 1
            
        return result