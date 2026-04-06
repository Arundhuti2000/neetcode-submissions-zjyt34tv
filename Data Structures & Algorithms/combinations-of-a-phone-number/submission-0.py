class Solution:
    def backtrack(self,ans, digitTostring, index, curr, digits):
        if len(curr)==len(digits):
            ans.append(curr)
            return
        currentDigit = digits[index]
        currentString = digitTostring[currentDigit]
        for i in range(len(currentString)):
            char = currentString[i]
            self.backtrack(ans, digitTostring, index+1, curr+char, digits)
        return
    def letterCombinations(self, digits: str) -> List[str]:
        
        if len(digits)==0:
            return []
        ans=[]
        digitTostring={"2":"abc","3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz" }
        self.backtrack(ans, digitTostring, 0, "", digits)
        return ans