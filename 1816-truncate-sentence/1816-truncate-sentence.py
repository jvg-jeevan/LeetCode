class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
# split() the string s to list
        list1 = s.split(' ')
# # if length of list is greater than k then pop() the last element and reutrn lit by converting it to string
#         while len(list1) > k:
#             list1.pop()
#         return ' '.join(list1)

        return ' '.join(list1[:k])
# return the string upto the length of k