class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        # drank = 0
        # empty = 0
        # while numBottles > 0:
        #     drank += numBottles
        #     total = numBottles + empty
        #     numBottles = total // numExchange
        #     empty = total % numExchange
        # return drank

        total = numBottles  # Total bottles drank
        while numBottles >= numExchange:
            exchanged = numBottles // numExchange  # Number of bottles exchanged
            total += exchanged  # Add exchanged bottles to total
            numBottles = exchanged + numBottles % numExchange  # Calculate remaining bottles after exchange
        return total