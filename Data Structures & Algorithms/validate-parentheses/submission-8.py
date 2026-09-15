class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) <= 1:
            return False 

        for char in s:
            # add in char if opening bracket
            if char == '[' or char == '(' or char =='{':
                stack.append(char)

            # get top item
            if len(stack) == 0:
                return False
            else:
                top_item = stack[-1]

            # Check for brackets
            if char == ']':
                if top_item != '[':
                    return False
                else:
                    stack.pop()

            # Check for parentheses
            if char == ')':
                if top_item != '(':
                    return False
                else:
                    stack.pop()

            # check for curly braces
            if char == '}':
                if top_item != '{':
                    return False
                else:
                    stack.pop()
        if len(stack) == 0:
            return True   
        else:
            return False 