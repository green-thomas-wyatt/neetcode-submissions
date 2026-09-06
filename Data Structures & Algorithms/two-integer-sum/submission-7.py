class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hash map where i keep track of the num and its index
        hash_set = {}

        for i in range(len(nums)):
            needed_num = target - nums[i]
            if needed_num in hash_set:
                return [hash_set[needed_num], i]
            else:
                hash_set[nums[i]] = i
        return []