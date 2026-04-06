class Solution:
    def backtrack(self,ans:List[int], cur:List[int], candidates:List[int],target:int, index:int, sum:int):
        if sum == target:
            ans.append(cur[:])
            return
        elif (sum < target):
            for i in range(index, len(candidates)):
                cur.append(candidates[i])
                self.backtrack(ans, cur, candidates, target,i, sum+candidates[i])
                cur.pop()
        return ans
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        cur=[]
        self.backtrack(ans, cur, candidates,target, 0, 0)
        return ans
