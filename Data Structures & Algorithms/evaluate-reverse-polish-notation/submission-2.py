import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if tokens is None:
            return 0
        stack = []
        operators= {
            '+': lambda y, x: y + x,
            '-': lambda y, x: y - x,
            '*': lambda y, x: y * x,
            '/': lambda y, x: int(y / x)
        }
        for token in tokens:
            if token in operators:
                x=stack.pop()
                y=stack.pop()
                print(token)
                stack.append(operators[token](y, x))
            else:
                stack.append(int(token))
        return stack.pop()
            