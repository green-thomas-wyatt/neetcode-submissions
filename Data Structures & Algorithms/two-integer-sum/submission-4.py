class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # I could make a nested for loop, but I know it is inefficnet
        # but for the practice, lets try it
        answer = []
        for x in range(len(nums)):
            for y in range(x + 1, len(nums)):
                if nums[x] + nums[y] == target:
                    return[x,y]
        print(answer)
        return []
        