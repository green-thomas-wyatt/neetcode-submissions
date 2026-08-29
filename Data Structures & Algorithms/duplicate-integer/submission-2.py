class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort Nums
        nums.sort()
        # Iterate through, if current is equal to next, the return true
        for x in range(len(nums)-1):
            if nums[x] == nums[x+1]:
                return True
        return False