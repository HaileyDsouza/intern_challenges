def isValid(s):
    stack = []
    pair = {
        '(' : ')',
        '[' : "]",
        '{' : '}'
    }
    for i in s:
        if i in pair:
            stack.append(i)
        elif len(stack) == 0 or i != pair[stack.pop()]:
            return False
    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))

 
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""