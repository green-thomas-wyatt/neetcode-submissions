class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        mid = (l+r) // 2

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)

        # lets look left and right of mid
        # or maybe we could look at l and r themselves

        # 3,4,5,6,1,2
        # mid would be 0 + 5 // 2 = 2, mid = 5
        # maybe lets look at l and r
        # we see if l > r, then l = mid?


        # 4,5,6,7
        # mid would be 0 + 3 // 2 = 1, mid = 5
        # if l < r, then r = mid?

        # Lets code it up now
        # ohh, we need a new condition for the while loop
        while l != r:
            mid = (l+r) // 2
            # Normal order
            if nums[l] < nums[r]:
                r = mid
            # It has been rotated
            if nums[l] > nums[r]:
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]


        