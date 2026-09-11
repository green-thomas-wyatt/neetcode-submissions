class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test_hash_set = set()
        best = 0
        L = 0
        
        # R naturally iterates through the string from 0 to len(s) - 1
        for R in range(len(s)):
            # If a duplicate is found, shrink the window from the left 
            # until the duplicate is removed from the set.
            while s[R] in test_hash_set:
                test_hash_set.remove(s[L])
                L += 1
                
            # Add the new character to the set
            test_hash_set.add(s[R])
            
            # Update the maximum length found so far
            # The current window length is R - L + 1
            best = max(best, R - L + 1)
            
        return best