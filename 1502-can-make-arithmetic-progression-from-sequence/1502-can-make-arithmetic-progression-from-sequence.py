class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
# for AP difference between current and next element should be same for all the elements
        arr.sort()
# sort the arr elements in ascending order
        d = arr[1] - arr[0]
# get the difference d

        result = True
# if the difference b/n current and next element is not equal to d break the loop and i.e not AP
        for i in range(len(arr)-1):
            if arr[i+1] - arr[i] != d:
                result = False
                break
        return result
# if all elements satisfies condition then return True