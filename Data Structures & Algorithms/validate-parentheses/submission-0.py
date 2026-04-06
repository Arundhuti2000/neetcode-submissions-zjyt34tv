class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if top!=bracket_map[char]:
                    return False
        return not stack
