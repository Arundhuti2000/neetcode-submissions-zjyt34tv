class Solution:
    def numWays(self,i,dp):
        if i==0:
            return 1
        if i == 1:
            return 1
        if dp[i] is not None:
            return dp[i]
        dp[i]=self.numWays(i-1,dp)+self.numWays(i-2,dp)
        return dp[i]
    def climbStairs(self, n: int) -> int:
        dp=[None]*(n+1)
        return self.numWays(n,dp) 