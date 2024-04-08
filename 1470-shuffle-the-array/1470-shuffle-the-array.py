class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    # divide the list nums into 2 parts
        num1 = nums[:n]
        num2 = nums[n:]
        res = []
        # zip() gets each element from num1 and num2 at a time 
        for x, y in zip(num1, num2):
            # extend the list res with x and y
            res.extend([x, y])
        return res