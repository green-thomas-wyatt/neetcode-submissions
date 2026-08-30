class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If not same legth, return false
        if len(s) != len(t):
            return False
        # Make a dict(hash map)
        # Iterate for each letter
        test_dict_s = {}
        test_dict_t = {}
        for char in s:
            test_dict_s[char] = test_dict_s.get(char, 0) +1
        for char in t:
            test_dict_t[char] = test_dict_t.get(char, 0) +1
        return test_dict_s == test_dict_t
     #test_dict_t[t[i]] += 1   

        
