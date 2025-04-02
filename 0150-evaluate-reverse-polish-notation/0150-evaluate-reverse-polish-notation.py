class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ele in tokens:
            if ele not in "+-*/":
                stack.append(int(ele))
            elif ele == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif ele == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif ele == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif ele == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack[0]