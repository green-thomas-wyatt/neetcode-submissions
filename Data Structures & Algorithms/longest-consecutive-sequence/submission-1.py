class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        ## Lets make this a set, for fast lookups
        nums_set = set(nums)
        # Lets check if it is a start of a sequence
        for num in nums_set:
            temp_max = 0
            if num-1 not in nums_set:
                current = num
                while(current in nums_set):
                    current += 1
                    temp_max += 1
                    if temp_max > max_seq:
                        max_seq = temp_max
        return max_seq

