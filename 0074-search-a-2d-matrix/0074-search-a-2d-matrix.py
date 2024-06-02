class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        # unpack the matrix into 1d list
        for row in matrix:
            arr.extend(row)


        # # if element in arr then return True or else False
        # if target in arr:
        #     return True
        # else:
        #     return False


# binary search
        low, mid, high = 0, 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return True
            
            elif arr[mid] < target:
                low = mid + 1

            else:
                high = mid - 1

        return False