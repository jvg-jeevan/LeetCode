class Solution:
    def digitSum(self, string: str, k: int) -> str:

# if input length is less than or equal to k return string as it is
# continue the execution only when len(string) > k
        while len(string) > k:
# map() each char to int and convert that to list
            result = list(map(int, string))

# split the list into nested list of desired size (in intervals of k)
            result = [result[i:i+k] for i in range(0, len(result), k)]

# get the sum of each nested list and map() to str
            result = list(map(str, [sum(row) for row in result]))

# join() every element from result and assign to string
            string = ''.join(result)

# reutrn the resultant string
        return string