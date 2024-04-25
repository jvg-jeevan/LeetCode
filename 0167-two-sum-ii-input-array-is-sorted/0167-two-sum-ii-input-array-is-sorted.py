class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
# binary search approach
# initialize left and right pointers
        left = 0
        right = len(numbers) - 1

# continue until you get the equal
        while left < right:
# get the sum of numbers
            total = numbers[left] + numbers[right]
# if total equals to sum then return the index
            if total == target:
                return [left + 1, right + 1]
# if total is greater than target then decrease right pointer (move towards smaller value)
            elif total > target:
                right -= 1
# if total is less than target then increase left pointer (move towards greater value)
            else:
                left += 1