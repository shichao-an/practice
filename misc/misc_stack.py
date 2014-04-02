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


if __name__ == '__main__':
    s1 = 'A*B-(C+D)+E'
    r1 = infix_to_postfix(s1)
    s2 = 'A*(B-C)+D-E*F'
    r2 = infix_to_postfix(s2)
    print(r1)
    print(r2)
    p1 = '123*+5-'
    print(postfix_eval(p1))
