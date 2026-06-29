class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "/":
                b, a = stack.pop(), stack.pop()
                # b is the demonitor because of RPM standard and stack
                stack.append(int(float(a/b)))
            else:
                stack.append(int(token))

        return stack[0]        