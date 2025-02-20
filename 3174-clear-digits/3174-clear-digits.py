class Solution:
    def clearDigits(self, s: str) -> str:
        # initialize empty stack
        stack = []
        for i in s:
            # if the element is alphabet then push to stack
            if i.isalpha():
                stack.append(i)
            # if digit then pop the top alphabet
            else:
                stack.pop()
        res = ''.join(stack)
        return res