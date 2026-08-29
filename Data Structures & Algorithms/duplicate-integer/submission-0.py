class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # declare hash map
        test_hash_set = set()
        # Iterate through hash map
        for int in nums:
        # Make key for each value, if key alreay exists return True
            if int in test_hash_set:
                return True
            else:
                test_hash_set.add(int)
        # Return False
        return False
