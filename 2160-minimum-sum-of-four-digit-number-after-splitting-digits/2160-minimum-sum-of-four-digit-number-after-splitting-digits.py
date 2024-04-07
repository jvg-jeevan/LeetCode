class Solution:
    def minimumSum(self, num: int) -> int:
# conver the number to list of str(each digit)
        arr = list(map(str, str(num)))
# sort() the list
        arr.sort()
# minimum sum is (1st, 3rd) digit and (2nd, 4th) digits
        return int(arr[0]+ arr[2]) + int(arr[1] + arr[3])