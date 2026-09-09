class Solution:
    def trap(self, height: List[int]) -> int:
        ## TWO POINTER APPROACH
        # min(height[L],height[R]) - height[i]

        L = 0
        R = len(height) - 1
        left_max = height[0]
        right_max = height[len(height) - 1]
        total = 0

        while L < R:
            if left_max <= right_max:
                L += 1
                total += max((left_max - height[L]), 0)
                if height[L] > left_max:
                    left_max = height[L]
            elif right_max < left_max:
                R -= 1
                total += max((right_max - height[R]), 0)
                if height[R] > right_max:
                    right_max = height[R]
        return total

