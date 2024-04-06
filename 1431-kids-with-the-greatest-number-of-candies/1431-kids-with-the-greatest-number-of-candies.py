class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        new_list = []

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max(candies):
                new_list.append(True)
            else:
                new_list.append(False)

        return new_list