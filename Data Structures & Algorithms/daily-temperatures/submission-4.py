class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        final_list = [0] * len(temperatures)
        # iterate through every elemnt
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_day = stack.pop()
                final_list[prev_day] = i-prev_day

            stack.append(i)


        return final_list