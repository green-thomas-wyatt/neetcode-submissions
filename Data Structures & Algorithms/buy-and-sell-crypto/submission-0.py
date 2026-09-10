class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute Force this?

        current_best = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                current_best = max(prices[j]-prices[i], current_best)
        return current_best

