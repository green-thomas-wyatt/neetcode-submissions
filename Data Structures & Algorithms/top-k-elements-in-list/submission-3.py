class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # SORTING METHOD/BRUTE FORCE

        # Hash map for sure, one pass and the i can return the the biggest value
        # in the value set of the hash map

        #test_hash = {}
        #for num in nums:
        #    test_hash[num] = test_hash.get(num, 0) + 1
        #top_x_keys = sorted(test_hash, key=test_hash.get, reverse = True)[:k]
        #print(top_x_keys)
        #return top_x_keys


        ## Maybe Optimal Solution Idk
        # Step 1: Build Frequency Map
        # Step 2: Create a list of len(nums) + 1 empty lists
        # Look through frequency map, and put each number in its bucket
        # Grab k values from back of array
        frequency_map = {}

        # Step 1: Build Frequency Map
        for num in nums:
            frequency_map[num] = frequency_map.get(num, 0) + 1
        
        # Step 2: Create a list of len(nums) + 1 empty lists
        list_test = [[] for i in range(len(nums)+1)]

        # Look through frequency map, and put each number in its bucket
        for key, value in frequency_map.items():
            list_test[value].append(key)

        # Grab k values from back of array
        tracker = 0
        final_list = []
        for item in reversed(list_test):
            if tracker == k:
                break
            elif item is None:
                continue
            else:
                for number in item:
                    if tracker != k:
                        final_list.append(number)
                        tracker += 1
                    else:
                        break
        return(final_list)

