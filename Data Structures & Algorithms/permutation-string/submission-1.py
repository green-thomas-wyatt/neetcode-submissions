class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ### Hmm brute force here
        # i can sort both string, and then interate through the second
        # and see if it contains the first

        s1_sorted = sorted(s1)
        print(s1_sorted)
        s2_sorted = sorted(s2)
        print(s2_sorted)

        L, R = 0, len(s1)
        while R <= len(s2):
            if s1_sorted == sorted(s2[L:R]):
                return True
            else:
                L+= 1
                R += 1
        return False

