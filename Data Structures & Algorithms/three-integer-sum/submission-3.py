class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ### HMMMM
        # Lets think brute force here
        # alright i am just going to try to solve it screw it

        # Sort list, and the maybe use 2 sum logic in some way?
        nums = sorted(nums)
        final_list = []
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1

            while left<right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    final_list.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    while nums[right] == nums[right+1] and right > left:
                        right -=1
                elif total < 0:
                    left += 1
                
                elif total > 0:
                    right -= 1

        return final_list