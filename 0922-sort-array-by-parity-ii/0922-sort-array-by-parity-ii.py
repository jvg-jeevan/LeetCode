class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
# separate the even and odd numbers into separate list
        evens = list(filter(lambda x: x%2 == 0, nums))
        odds = list(filter(lambda x: x%2 != 0, nums))
# empty the list nums
        nums.clear()
# zip() takes each element from both evens and odds
        for i, j in zip(evens, odds):
# add the element to nums first (even index) even number , second (odd index) odd number 
            nums.append(i)
            nums.append(j)
# return the nums list
        return nums