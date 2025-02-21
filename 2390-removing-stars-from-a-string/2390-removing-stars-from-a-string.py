class Solution:
    def removeStars(self, s: str) -> str:

        # create an empty stack
        stack = []
        # convert the string to array
        arr = list(s)
        
        # iterate through each element in the list
        for i in range(len(arr)):

            # if an alphabet then push onto stack 
            if arr[i].isalpha():
                stack.append(arr[i])
            # if not pop the top element of the stack
            else:
                stack.pop()

        # return the string by joining elements of stack
        return ''.join(stack)