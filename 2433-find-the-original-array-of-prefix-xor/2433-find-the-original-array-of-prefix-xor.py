class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
    # create an arr list to store the xor numbers initialize all numbers to 0
        arr = [0] * n
        xor = 0
        # xor to initialize the xor operation (changed after each operation)
        for i in range(n):
# for each element in list pref get the xor and store in arr at ith position
            arr[i] = xor ^ pref[i]
# xor ^ arr[i] will be the new xor value
            xor ^= arr[i]
        return arr