class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(sorted(str(n))))
# according to hint max digit will be answer