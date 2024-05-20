class Solution:
    def digitSum(self, string: str, k: int) -> str:

        while len(string) > k:

            result = list(map(int, string))

            result = [result[i:i+k] for i in range(0, len(result), k)]

            result = list(map(str, [sum(row) for row in result]))

            string = ''.join(result)

        return string