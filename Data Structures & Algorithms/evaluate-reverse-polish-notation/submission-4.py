import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
      
        stack = []

        for sym in tokens:
            if sym in ("+", "-", "*", "/"):
                b = stack.pop()
                a = stack.pop()
                if sym == "+":
                    stack.append(a+b)
                if sym == "-":
                    stack.append(a-b)
                if sym == "*":
                    stack.append(a*b)
                if sym == "/":
                    if b == 0:
                        stack.append(0)
                    else:
                        stack.append(int(a/b))
            else:
                stack.append(int(sym))
        

        

        return stack[0]