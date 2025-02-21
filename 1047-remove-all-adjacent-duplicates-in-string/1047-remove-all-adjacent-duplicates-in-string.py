class Solution:
    def removeDuplicates(self, s: str) -> str:
        # create empty stack
        stack = []
        # take each char in string 
        for i in s:
            # if char not in stack push 
            if (not stack) or (stack[-1] != i):
                stack.append(i)
            # if top of stack == current char pop
            elif stack[-1] == i:
                stack.pop()
        # return the resulting string from stack
        return ''.join(stack)