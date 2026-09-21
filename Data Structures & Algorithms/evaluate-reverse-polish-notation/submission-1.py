class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        ## Push all the numbers until you hit an operator
        # when you hit an operator, pop until stack is empty
        # start pushing again and repeat
        # eval()

        total = 0
        expression = ""

        for token in tokens:
            if token != '+' and token != '-' and token != '*' and token != '/':
                stack.append(int(token))
            else:
                a = stack.pop()
                b = stack.pop()
                if token == "+":
                    res = a + b
                elif token == "-":
                    res = b - a
                elif token == "*":
                    res = a * b
                elif token == "/":
                    res = int(b/a)
                stack.append(res)

        
        return stack[0]