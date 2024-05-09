class Solution:
    def search(self, nums: List[int], target: int) -> int:

# initialize low, high and mid
        low = 0
        high = len(nums) - 1
        mid = 0
        
        while low <= high:
            mid = (low + high) // 2

# if mid is less than target, low will be next to mid
            if nums[mid] < target:
                low = mid + 1

# if mid is high than target, high will be previous to mid
            elif nums[mid] > target:
                high = mid - 1

# if target = mid, return mid
            else:
                return mid
# if element not found return -1   
        return -1