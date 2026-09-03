class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ok lets try to implement this prefix suffix technqiue

        # Declare arrays
        prefix_array = []
        suffix_array = [0] * len(nums)

        #Prefix loop
        prefix_num = 1

        for i in range(len(nums)):
            prefix_array.append(prefix_num)
            prefix_num *= nums[i]

        #Suffix Loop
        suffix_num = 1
        for i in range(len(nums) -1, -1, -1):
            suffix_array[i] = suffix_num
            suffix_num *= nums[i]

        result = []
        for i in range(len(suffix_array)):
            result.append(prefix_array[i] * suffix_array[i])
        return(result)
