class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_value = float("inf")
        for price in prices:
            if price < buy_value:
                buy_value = price
            profit = max(profit, price - buy_value)
        return profit