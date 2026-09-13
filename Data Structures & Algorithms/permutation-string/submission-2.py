class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        arr_s1 = [0] * 26
        arr_s2 = [0] * 26

        # initlaize both arrays with the value counts for len(s1)
        for i in range(len(s1)):
            index_s1 = ord(s1[i]) - ord('a')
            index_s2 = ord(s2[i]) - ord('a')
            arr_s1[index_s1] += 1
            arr_s2[index_s2] += 1

        if arr_s1 == arr_s2:
            return True

        #index = ord(letter) - ord(a)
        for R in range(len(s1), len(s2)):
            index = ord(s2[R - len(s1)]) - ord('a')
            arr_s2[index] -= 1
            index = ord(s2[R]) - ord('a')
            arr_s2[index] += 1
            if arr_s1 == arr_s2:
                return True
            
        return False