def isValid(s):
    is_valid = False
    for i in range(len(s)):
        if s[i] == "(" and s[i+1] == ")":
            is_valid = True
        if s[i] == "{" and s[i+1] == "}":
            is_valid = True
        if s[i] == "[" and s[i+1] == "]":
            is_valid = True
    return is_valid
       
print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))