class Solution:

    def encode(self, strs: List[str]) -> str:
        # I could brute force this, iterate through every char, right?
        # Should I include a space, i think I will.
        ## BRUTE FORCE

        # Check is strs is empty
        #if not strs:
            # if it is return a char outside of the 256 ascii charaters
        #    return chr(258)
        # Otherwise use chr 257 as a delimiter to we can split on it later
        #return (chr(257).join(strs))

        ## NON-BRUTE FORCE/OPTIMAL
        # for each str, prepend the length and a # or something like that
        fin_str = ""
        for word in strs:
            fin_str += str(len(word))
            fin_str += "#"
            fin_str += word
        return(fin_str)
        


    def decode(self, s: str) -> List[str]:
        ## BRUTE FORCE
        # Now I do the opposite, i can iterate throguh each char, and when
        # there is a space, i make a new list
        #if s == chr(258):
        #    return []
        #return(s.split(chr(257)))

        ## NON-BRUTE FORCE/OPTIMAL

        # declare return list
        final_list = []
        # Declare incermenter 1
        i = 0

        # while i is less than total length of s
        while i < len(s):
            # start pointer 2, to help track length
            j = i
            # Iterate j until it finds #, this will give us
            # the length of the str(i:j)
            while s[j] != "#":
                j += 1
            # Now that we have the string length, we can grab the word
            length = int(s[i:j])
            # set i equal to first char of the word
            i = j+1
            # set j equal to the last char of the word
            j = i + length
            final_list.append(s[i:j])
            i = j
        return(final_list)

            
