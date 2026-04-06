class Solution:
    def is_palindrome(self, s:str)-> bool:
        return s == s[::-1]
    def backtrack(self, ans, cur, s, index):
        if index == len(s):
            ans.append(cur[:])
            return ans
        for i in range(index,len(s)):
            substring = s[index : i + 1]
            if self.is_palindrome(substring):
                cur.append(substring)
                self.backtrack(ans, cur, s, i+1)
                cur.pop()
        return ans
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        cur=[]
        self.backtrack(ans, cur, s, 0)
        return ans