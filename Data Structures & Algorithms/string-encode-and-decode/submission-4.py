class Solution:

    def encode(self, strs: List[str]) -> str:
        # I could brute force this, iterate through every char, right?
        # Should I include a space, i think I will.
        if not strs:
            return chr(258)
        return (chr(257).join(strs))
        


    def decode(self, s: str) -> List[str]:
        ## BRUTE FORCE
        # Now I do the opposite, i can iterate throguh each char, and when
        # there is a space, i make a new list
        if s == chr(258):
            return []
        return(s.split(chr(257)))
            
