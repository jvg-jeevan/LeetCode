class Solution:
    def evenOddBit(self, n: int) -> List[int]:
# res list to store the binary representation
        res = []
        while n != 0:
            res.append(n % 2)
            n //= 2
# even and odd to store the count
        even = 0
        odd = 0
# iterate through each element in res check if 1 and also even or odd index and increment
        for i in range(len(res)):
            if (i % 2 == 0) and (res[i] == 1):
                even += 1
            elif (i % 2 != 0) and (res[i] == 1):
                odd += 1

# return the list with even, odd count
        return [even, odd]