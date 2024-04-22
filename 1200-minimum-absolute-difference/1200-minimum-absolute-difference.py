class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
# sort the elemetns in ascending order
        arr.sort()
# result list to store pairs
        result = []
# diff stores the initial difference of first two elements
        diff = arr[1] - arr[0]
# iterate through the elements current and next element
        for i in range(len(arr)-1):
# curr_diff stores the difference b/n the current and next element
            curr_diff = abs(arr[i+1] - arr[i])
# if curr_diff is less than initial diff then update the diff 
            if curr_diff < diff:
                diff = curr_diff
# result.clear() beacause to clear the pairs those difference less than current
                result.clear()
# append() the current pairs
                result.append([arr[i], arr[i+1]])

# if diff is equal to curr_diff then append() the pairs
            elif curr_diff == diff:
                result.append([arr[i], arr[i+1]])
            
# return the resultant pairs
        return result