def isValid(s: str) -> bool:
    stack = []
    bracket_map = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in bracket_map:
            top_element = stack.pop() if stack else '#'
            if bracket_map[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack


user_input = input("Enter a string of brackets (only (), {}, []): ").strip()
result = isValid(user_input)


print("Valid" if result else "Invalid")
