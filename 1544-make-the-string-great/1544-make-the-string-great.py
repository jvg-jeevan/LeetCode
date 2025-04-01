class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for i in s:
            if i.islower():
                stack.append(i)
            elif stack and stack[-1] == i.lower():
                stack.pop()
            else:
                pass
        return ''.join(stack)