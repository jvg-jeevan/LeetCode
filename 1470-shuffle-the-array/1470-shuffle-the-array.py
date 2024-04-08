class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
    # divide the list nums into 2 parts
        num1 = nums[:n]
        num2 = nums[n:]
        res = []
        # zip() gets each element from num1 and num2 at a time 
        for x, y in zip(num1, num2):
            # append x and y to res
            res.append(x)
            res.append(y)
        return res