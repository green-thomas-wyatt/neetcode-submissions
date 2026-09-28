class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_speed = max(piles)

        # Binary Search 
        left = 1
        right = max_speed
        mid = (left + right) // 2

        while left < right:
            # Calculate mid
            mid = (left + right) // 2
            # Calculcate the score of the mid speed
            mid_score = sum((pile + mid -1) // mid for pile in piles)

            # If it is less than or equal to h, there could be something smaller still
            if mid_score <= h:
                right = mid

            if mid_score > h:
                left = mid + 1
        return left


