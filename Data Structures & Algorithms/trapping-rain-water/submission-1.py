class Solution:
    def trap(self, height: List[int]) -> int:
        # height = min(height[L],height[R]) - height[i]
        # Lets pre computer stuff here
        total = 0
        tallest = 0
        left_maxes = []
        right_maxes = []

        # LEFT MAX
        for i in range(len(height)):
            if i == 0:
                left_maxes.append(height[i])
                tallest = height[i]
            else:
                if height[i] > tallest:
                    tallest = height[i]
                    left_maxes.append(height[i])
                else:
                    left_maxes.append(tallest)
        # RIGHT MAX 
        tallest = 0
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                right_maxes.append(height[i])
                tallest = height[i]
            else:
                if height[i] > tallest:
                    tallest = height[i]
                    right_maxes.append(height[i])
                else:
                    right_maxes.append(tallest)
        
        for i in range(len(height)):
            total += max(min(left_maxes[i], right_maxes[len(height) - 1 -i]) - height[i] , 0)

        return total