class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # result = True
        # arr.sort(reverse = True)
        # for i in range(len(arr)-1):
        #     if arr[i] == 0:
        #         break
        #     for j in range(i+1, len(arr)):
        #         if arr[j] == 0:
        #             break
        #         elif (arr[i] == 2*arr[j]) or (arr[j] == 2 * arr[i]):
        #             result = True
        #             break
        #         else:
        #             result = False

        #     if result:
        #         break
        # return result

# i in range(len(arr)), j in range(i), check for condition i.e number is double
# if any one is double retrun True else False
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] == 2 * arr[j] or arr[j] == 2 * arr[i]:
                    return True
        return False