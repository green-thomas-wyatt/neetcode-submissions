class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hash map for sure, one pass and the i can return the the biggest value
        # in the value set of the hash map
        test_hash = {}
        for num in nums:
            test_hash[num] = test_hash.get(num, 0) + 1
        #sorted_list = sorted(test_hash.values(), reverse = True)
        top_x_keys = sorted(test_hash, key=test_hash.get, reverse = True)[:k]
        print(top_x_keys)
        return top_x_keys