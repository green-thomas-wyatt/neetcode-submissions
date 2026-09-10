class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L, R = 0,1

        best_price = 0

        while R < len(prices):
            if prices[R] > prices[L]:
                best_price = max(prices[R] - prices[L], best_price)
            elif prices[R] < prices[L]:
                L = R
            R += 1
        return best_price