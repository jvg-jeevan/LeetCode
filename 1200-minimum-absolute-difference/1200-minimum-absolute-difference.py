class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        result = []
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            each_diff = abs(arr[i+1] - arr[i])
            if each_diff < diff:
                diff = each_diff
                result.clear()
                result.append([arr[i], arr[i+1]])

            elif each_diff == diff:
                result.append([arr[i], arr[i+1]])
            
                
        return result