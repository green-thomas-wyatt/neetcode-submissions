class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest_seen = float('inf')
        best_price = 0

        for i in range(len(prices)):
            cheapest_seen = min(cheapest_seen, prices[i])
            if prices[i] - cheapest_seen > best_price:
                best_price = prices[i] - cheapest_seen
        return best_price