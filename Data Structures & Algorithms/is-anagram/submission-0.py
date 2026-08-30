class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If not same legth, return false
        if len(s) != len(t):
            return False
        # Make a dict(hash map)
        # Iterate for each letter
        test_dict_s = {}
        test_dict_t = {}
        for i in range(len(s)):
            if s[i] in test_dict_s:
                test_dict_s[s[i]] += 1
            else:
                test_dict_s[s[i]] = 1
            if t[i] in test_dict_t:
                test_dict_t[t[i]] += 1
            else:
                test_dict_t[t[i]] = 1
        print(test_dict_s, test_dict_t)
        if(test_dict_s == test_dict_t):
            return True
        else:
            return False
     #test_dict_t[t[i]] += 1   

        
