class Solution:
    def coins(self, coins, remaining,memo):
        if remaining <0: return -1
        if remaining ==0: return 0
        if remaining in memo:
            return memo[remaining]
        min_coin=math.inf
        for coin in coins:
            result = self.coins(coins, remaining - coin,memo)
            if (result>=0) and ((1 + result)<min_coin):
                min_coin=min(min_coin, 1 + result)
        memo[remaining] = min_coin
        return min_coin

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount<1:
            return 0
        memo = {}
        final_result = self.coins(coins, amount, memo)
        return final_result if final_result != math.inf else -1