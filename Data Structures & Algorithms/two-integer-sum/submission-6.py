class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## BRUTE FORCE
        # I could make a nested for loop, but I know it is inefficnet
        # but for the practice, lets try it
        #for x in range(len(nums)):
        #    for y in range(x + 1, len(nums)):
        #        if nums[x] + nums[y] == target:
        #            return[x,y]
        #print(answer)
        #return []

        # HASHMAP
        # I can put all the numbers in a hash map as I go along
        # For the current number, if the number needed to get to target
        # is already in the hash map, then return those two numbers

        # Declare hash map
        # I will need a current number needed varibale also
        test_hash = {}
        # check if the number is already in it(could cause issues with duplicates)
        for i in range(len(nums)):
            # get our needed number
            needed_num = target - nums[i]
            # if it is in the dict, we need to get the index and the current index
            if needed_num in test_hash:
                return[test_hash[needed_num], i]
            else:
                test_hash[nums[i]] = test_hash.get(nums[i], i)
        return []



        
        