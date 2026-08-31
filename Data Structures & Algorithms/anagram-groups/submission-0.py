class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## SORTING SOLUTION
        # Declare hash map
        test_hash = {}
        #declare return list
        final_list = []
        # Iterate through list, sort each word, and turn it into a tuple
        # Use tuple as
        for word in strs:
            new_word = tuple(sorted(word))
            test_hash[new_word] = test_hash.get(new_word, []) + [word]
        return list(test_hash.values())

        

    
    # hash of some kind
    # hash set or hash map?
    # go through each word and make it into a dict
    # the loop through again and if they are equal, add them to a new list

     #   answer_list = []
     #   for word in strs:
     #       temp_dict = {}
    #      for char in word:
    #            temp_dict[char] = temp_dict.get(char, 0) +1
    #        answer_list.append(temp_dict)
    #    for word_dict in answer_list:

    #    print(answer_list)

        return []
