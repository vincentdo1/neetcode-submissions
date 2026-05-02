class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount == 0):
            return 0
        if (amount < min(coins)):
            return -1
        dp = [10000] * (amount + 1)
        n = len(coins)
        dp[0] = 0
        for i in range(coins[0], amount + 1):
            for c in coins:
                if (i - c >= 0):
                    dp[i] = min(dp[i], dp[i - c] + 1)
        if (dp[-1] == 10000):
            return -1
        return dp[-1]