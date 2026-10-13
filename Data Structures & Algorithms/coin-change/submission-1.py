class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        def solve(idx, amt):
            if (idx, amt) in dp:
                return dp[(idx, amt)]
            if amt == amount:
                return 0
            if idx >= len(coins) or amt > amount:
                return float("inf")
            # skip
            skip = solve(idx + 1, amt)
            # pick
            pick = 1+ solve(idx, amt + coins[idx])
            dp[(idx, amt)] = min(skip, pick)
            return min(skip, pick)
        ans = solve(0,0)
        return -1 if ans == float("inf") else ans
        