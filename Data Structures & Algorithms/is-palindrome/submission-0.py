class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = 1
        s_good = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(s_good)):
            if s_good[i] == s_good[len(s_good) - j]:
                j += 1
                continue
            else:
                return False
            j += 1
        return True