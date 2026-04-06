class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brac={')':'(',
            '}':'{',
            ']':'['
        }
        for char in s:
            if char in brac.values():
                stack.append(char)
            elif char in brac:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if top!=brac[char]:
                    return False
            else:
                return False
        return not stack
