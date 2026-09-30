class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ## Lets set up a base like before
        l,r = 0 , len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Step 1: Check if LEFT half is sorted
            if nums[l] <= nums[mid]:
                # Is target inside the sorted left half?
                if target < nums[mid] and target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Step 2: Otherwise, RIGHT half must be sorted!
            else:
            # Is target inside the sorted right half?
                if target > nums[mid] and target <= nums[r]:
                    l = mid +1
                else:
                    r = mid - 1
        return -1
