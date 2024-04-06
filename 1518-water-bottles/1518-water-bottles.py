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
# Number of bottles exchanged 
            exchanged = numBottles // numExchange  
# Add exchanged bottles to total as exchanged bottles will be dranked
            total += exchanged  
# Calculate remaining bottles after exchange i.e exchanged bottles and remaining bottles couldnot exchanges
            numBottles = exchanged + numBottles % numExchange  
        return total