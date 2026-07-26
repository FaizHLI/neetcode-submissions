class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #if its an operand, pop the last two arguments and do the operation
        #push the result and return top of the stack
        stack = []
        for t in tokens:
            if t == "+":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 + op2)
            elif t == "-":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op1 - op2)
            elif t == "*":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op1 * op2)
            elif t == "/":
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(int(float(op1)/ op2))
            else:
                stack.append(int(t))
        return stack[-1]