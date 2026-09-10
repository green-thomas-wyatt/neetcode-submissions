class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prefix = []
        suffix = []
        
        #PREFIX ARRAY
        cheapest_seen = 0
        for i in range(len(prices)):
            if i == 0:
                cheapest_seen = prices[i]
                prefix.append(cheapest_seen)
            else:
                if prices[i] < cheapest_seen:
                    cheapest_seen = prices[i]
                    prefix.append(cheapest_seen)
                else:
                    prefix.append(cheapest_seen)

        #SUFFIX ARRAY
        expensive_seen = 0
        for i in range(len(prices) -1, -1, -1):
            if i == len(prices) -1:
                expensive_seen = prices[i]
                suffix.append(expensive_seen)
            else:
                if prices[i] > expensive_seen:
                    expensive_seen = prices[i]
                    suffix.append(expensive_seen)
                else:
                    suffix.append(expensive_seen)
        suffix.reverse()

        best_seen = 0
        for i in range(len(prices)):
            if suffix[i] - prefix[i] > best_seen:
                best_seen = suffix[i] - prefix[i]

        return best_seen