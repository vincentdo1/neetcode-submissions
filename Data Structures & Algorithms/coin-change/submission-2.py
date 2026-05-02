class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if (amount == 0):
            return 0
        if (amount < min(coins)):
            return -1
        dp = [10000] * (amount + 1)
        n = len(coins)
        for i in range(n):
            if (coins[i] <= amount):
                dp[coins[i]] = 1
        for i in range(coins[0], amount + 1):
            for j in range(n):
                if (i - coins[j] >= 0):
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        print(dp)
        if (dp[-1] == 10000):
            return -1
        return dp[-1]