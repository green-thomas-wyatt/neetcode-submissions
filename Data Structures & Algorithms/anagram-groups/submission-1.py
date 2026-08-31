class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## SORTING SOLUTION
        # Declare hash map

        #test_hash = {}

        #declare return list

        #final_list = []

        # Iterate through list, sort each word, and turn it into a tuple
        # Use tuple as key, and append the words to it, then return

        # Time: O(n logn), because sorting

        #for word in strs:
        #    new_word = tuple(sorted(word))
        #    test_hash[new_word] = test_hash.get(new_word, []) + [word]
        #return list(test_hash.values())

        

    
        # Freqency Count Solution

        # initialziaze hash
        test_hash = {}
        # Iterate through each word
        for word in strs:
            # Define spots for all chars in the alphabet
            count = [0] * 26
            # iterate throgh each char
            for char in word:
                # increment the spot in the list where the letter corresponds
                count[ord(char)-ord('a')] += 1
            # Convert to tuple
            count_tuple = tuple(count)
            # Add to hash
            test_hash[count_tuple] = test_hash.get(count_tuple, []) + [word]
        return list(test_hash.values())
        

        


        return []
