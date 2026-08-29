class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Sort Nums
        nums_sorted = sorted(nums)
        # Iterate through, if current is equal to next, the return true
        for x in range(len(nums)-1):
            if nums_sorted[x] == nums_sorted[x+1]:
                return True
        return False