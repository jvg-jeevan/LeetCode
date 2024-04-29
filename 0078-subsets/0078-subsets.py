import itertools
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
# itertools.combinations(iterable, n) returns n length subsequences of elements from the input iterable.
        result = []
# result to store the lists
        for n in range(len(nums)+1):
# to get subsets of all lengths
            result.extend(list(itertools.combinations(nums, n)))
        return result