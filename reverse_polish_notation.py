#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        opts = set(['+', '-', '*', '/'])

        for i in range(len(tokens)):
            if tokens[i] in opts:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = a - b
                elif tokens[i] == '*':
                    c = 1.0 * a * b
                else:
                    c = 1.0 * a / b

                stack.append(int(c))
            else:
                stack.append(int(tokens[i]))

        return stack[-1]

if __name__ == '__main__':
    print Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
