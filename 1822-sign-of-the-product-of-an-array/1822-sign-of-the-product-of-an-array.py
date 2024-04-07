class Solution:
    def arraySign(self, nums: List[int]) -> int:
# intitalize the product to 1 
        product = 1
# for each element in list find the product by multiplying each element with each each, if any element in list is zero then the product becomes zero
        for i in nums:
            if i == 0:
                product = 0
                break
            product *= i

# return result as per condition
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
            