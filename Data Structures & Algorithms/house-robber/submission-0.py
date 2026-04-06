class Solution:
    def robhouse(self,houses, n,dp):
            if n==0:
                return 0
            dp[0]=houses[0]
            for i in range(1,n):
                if i==1:
                    dp[1]=max(houses[0],houses[1])
                else:
                    ith_houose_stolen=houses[i] + dp[i-2]
                    ith_houose_not_stolen=dp[i-1]
                    dp[i]=max(ith_houose_stolen,ith_houose_not_stolen)
            return dp[n-1]
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp = [None] * n
        return self.robhouse(nums, n,dp)