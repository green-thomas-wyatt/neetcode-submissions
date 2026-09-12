class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L, R = 0,0
        best = 0
        char_freq = {}
        # length of window - count of most frequent char
        while R < len(s):
            char_freq[s[R]] = char_freq.get(s[R], 0)+1
            len_of_window = R-L + 1
            k_tracker = max(char_freq.values())

            if(len_of_window - k_tracker <= k):
                best = max(len_of_window, best)
                R += 1
            else:
                char_freq[s[L]] -= 1
                L += 1
                R += 1
        return best
        