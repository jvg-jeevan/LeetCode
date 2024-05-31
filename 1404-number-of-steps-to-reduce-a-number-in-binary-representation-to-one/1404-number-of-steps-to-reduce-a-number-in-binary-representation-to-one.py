class Solution:
    def numSteps(self, s: str) -> int:
# convert the string s to list of type int and reverse the list
        s = list(map(int, s))[::-1]
# initialize the num to 0
        num = 0
# converting the binary format to int i.e for every binary digit 
        for ind, val in enumerate(s):
# num += val times two power of index
            num += (val * (2 ** ind))

# initialize res to zero   
        res = 0
# while num > 1 continue inside while loop
        while num > 1:
# if num becomes 1 break out of while and return the res
            if num == 1:
                break
# if num is even then reduce the num >> divides the num by two power 1
            elif num % 2 == 0:
                num >>= 1
# increment the res count to 1
                res += 1
# if num is odd then increment the num by 1 and also the res with 1
            else:
                num += 1
                res += 1
            
# return the res 
        return res