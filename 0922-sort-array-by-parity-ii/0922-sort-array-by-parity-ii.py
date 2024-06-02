class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        evens = list(filter(lambda x: x%2 == 0, nums))
        odds = list(filter(lambda x: x%2 != 0, nums))
        nums.clear()
        for i, j in zip(evens, odds):
            nums.append(i)
            nums.append(j)

        return nums