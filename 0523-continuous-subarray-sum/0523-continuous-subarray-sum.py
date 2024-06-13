class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
# initialize prefix sum to 0
        prefix_sum = 0
# Initialize a hash map to store remainders and their indices
# Key: Remainder of the prefix sum modulo k
# Value: Index where the corresponding remainder was first encountered.
        remainder_map = {0: -1}

# iterate through the list
        for i in range(len(nums)):
# calculate prefix_sum by adding the current element
            prefix_sum += nums[i]
# calculate the remainder when prefix_sum is divided by k
            remainder = prefix_sum % k

# if remainder already in remainder_map
            if remainder in remainder_map:
# check if length of subarray is atleast 2
                if i - remainder_map[remainder] > 1:
# if found any array satisfying condition then return true
                    return True 

# if remainder not in remainder_map
            else:
# then store the current index for the remainder
                remainder_map[remainder] = i
                
# if no array found then return False
        return False