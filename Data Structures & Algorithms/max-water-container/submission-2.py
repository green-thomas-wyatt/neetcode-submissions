class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Find the max at the same time
        # Two pointers here
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            width = abs(right-left)
            height = min(heights[left], heights[right])
            if (width * height > max_area):
                max_area = width * height
                print(max_area)
            if heights[left] < heights[right]:
                print(left)
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
                print(right)
            elif heights[right] == heights[left]:
                right -= 1
        return max_area