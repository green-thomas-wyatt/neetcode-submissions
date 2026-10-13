class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # slow takes 1 step, fast takes 2 steps from index 0
        slow = nums[0]
        fast = nums[nums[0]]
        
        # Phase 1: Meet in the cycle
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
        # Phase 2: Find the entrance to the cycle
        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
            
        return slow