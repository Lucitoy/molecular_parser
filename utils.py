def is_closing_char(char):
    closing_brackets = [')', ']', '}']
    return char in closing_brackets

def is_opening_char(char):
    opening_brackets = ['(', '[', '{']
    return char in opening_brackets

def are_brackets_matching(b1, b2):
    match = {'(': ')', '[': ']', '{': '}'}
    
    return is_opening_char(b1) and match[b1] == b2
