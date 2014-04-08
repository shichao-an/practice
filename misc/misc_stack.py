from __future__ import print_function


operators = {
    '(': 3,
    ')': 3,
    '*': 2,
    '/': 2,
    '+': 1,
    '-': 1,
}


# Assume all tokens are single-character

def infix_to_postfix(s):
    """Simple version of shunting-yard algorithm"""
    stack = []
    res = ''
    for c in s:
        if c not in operators:
            res += c
        elif c == ')':
            if stack:
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()  # Pop `(`
            else:
                raise Exception('mismatched parentheses')
        elif c == '(':
            stack.append(c)
        # c is an operator
        else:
            # Pop those on the stacks that have equal or higher
            # precedence than the current token
            # Stop if top of the stack is left parentheses
            while (stack and operators[stack[-1]] >= operators[c]
                   and stack[-1] != '('):
                res += stack.pop()
            stack.append(c)
    while stack:
        res += stack.pop()
    return res


def postfix_eval(s):
    stack = []
    for c in s:
        # c is an operand
        if c not in operators:
            stack.append(c)
        # Assume no unary operators
        else:
            o1 = stack.pop()
            o2 = stack.pop()
            stmt = o2 + c + o1  # o2 comes first
            res = str(eval(stmt))
            stack.append(res)
    return stack.pop()


class AdvancedStack(object):
    """Stack that has O(1) get_min() method"""
    def __init__(self):
        self.elem_stack = []
        self.min_stack = []

    def pop(self):
        popped = self.elem_stack.pop()
        # Pop the min_stack if the popped value from elem_stack is equal
        # to the current min value
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def push(self, data):
        if self.min_stack:
            # Only push to the min_stack if data is less than or equal
            # to the current min value
            if data <= self.min_stack[-1]:
                self.min_stack.append(data)
        else:
            self.min_stack.append(data)
        self.elem_stack.append(data)

    def get_min(self):
        return self.min_stack[-1]


def find_spans(A):
    """
    Given an array A, return array S, where S[i] of A[i] is the maximum number
    of consecutive elements immediately preceding A[i] and smaller than or
    equal to A[i]
    """
    stack = []
    n = len(A)
    S = [0] * n
    p = -1  # Index of the element which is greater than or equal to the
            # current element
    for i in range(n):
        print(stack)
        while stack and A[i] > A[stack[-1]]:
            stack.pop()
        if not stack:
            p = -1
        else:
            p = stack[-1]
        S[i] = i - p
        stack.append(i)
    return S


if __name__ == '__main__':
    s1 = 'A*B-(C+D)+E'
    r1 = infix_to_postfix(s1)
    s2 = 'A*(B-C)+D-E*F'
    r2 = infix_to_postfix(s2)
    print(r1)
    print(r2)
    p1 = '123*+5-'
    print(postfix_eval(p1))
    a = [6, 3, 4, 5, 2]
    s = find_spans(a)
    print(s)
