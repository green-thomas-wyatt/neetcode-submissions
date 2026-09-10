class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = []
        suffix = []
        
        #PREFIX ARRAY
        cheapest_seen = float('inf')
        for i in range(len(prices)):
            cheapest_seen = min(cheapest_seen, prices[i])
            prefix.append(cheapest_seen)

        #SUFFIX ARRAY
        expensive_seen = float('-inf')
        for i in range(len(prices) -1, -1, -1):
            expensive_seen = max(expensive_seen, prices[i])
            suffix.append(expensive_seen)
        suffix.reverse()

        best_seen = 0
        for i in range(len(prices)):
            if suffix[i] - prefix[i] > best_seen:
                best_seen = suffix[i] - prefix[i]

        return best_seen