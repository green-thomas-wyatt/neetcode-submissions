class Solution:
    def minWindow(self, s: str, t: str) -> str:
        best = ""
        if len(t) > len(s):
            return best
        if s == t:
            return s

        L = 0
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        required_chars = len(t_count)
        satisfied_chars = 0
        windows_count = {}

        for R in range(len(s)):
            c = s[R]
            windows_count[c] = windows_count.get(c, 0) + 1
            if c in t_count and windows_count[c] == t_count[c]:
                satisfied_chars += 1

            while satisfied_chars == required_chars:
                if best == "" or R - L + 1 < len(best):
                    best = s[L:R + 1]

                left_char = s[L]
                windows_count[left_char] -= 1   # ← was missing
                if left_char in t_count and windows_count[left_char] < t_count[left_char]:
                    satisfied_chars -= 1         # ← was typo
                L += 1

        return best