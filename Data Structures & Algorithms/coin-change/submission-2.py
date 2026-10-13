class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1, 5, 10

        #    0, 1, 2, 3(amount) 
        # 1  0, 1, 2, 3
        # 5  0, 
        # 10 0
        # (coins)

        m = amount + 1
        n = len(coins) + 1
        dp = [[0] * m for _ in range(n)]

        for i in range(1, m):
            dp[0][i] = float("inf")
        for coin in range(1, n):
            coin_val = coins[coin - 1]
            for amt in range(1, m):
                if amt - coin_val >= 0:
                    dp[coin][amt] = min(dp[coin - 1][amt], 1 + dp[coin][amt - coin_val])

                else:
                    dp[coin][amt] = dp[coin - 1][amt]
        return -1 if dp[n - 1][m - 1] == float("inf") else dp[n - 1][m - 1]
        