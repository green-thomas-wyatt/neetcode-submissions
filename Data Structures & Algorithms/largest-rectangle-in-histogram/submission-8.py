class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # We need to find the greatest L * W
        # we need to find 2 peeks 

        stack = []
        total = 0
        curr_total = 0

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]

        for index, height in enumerate(heights):

            if len(stack) == 0:
                stack.append((heights[0],index))
                continue

            # When the num is greater than top of stack
            if heights[index] < stack[-1][0]:
                while stack and heights[index] < stack[-1][0]:
                    h, i = stack.pop()
                    if stack:
                        width = index - stack[-1][1] - 1
                    else:
                        width = index
                    area = width * h

                    if area > total:
                        total = area
            stack.append((heights[index],index))

        # Cleanup Loop
        while stack:
            h, i = stack.pop()
            if stack:
                width = len(heights) - stack[-1][1] - 1
            else:
                width = len(heights)
            area = width * h
            if area > total:
                total = area
        

        return total