def is_closing_char(char):
    closingbrackets = [')', ']', '}']
    return char in closingbrackets

def is_opening_char(char):
    closingbrackets = ['(', '[', '{']
    return char in closingbrackets

def are_brackets_matching(b1, b2):
    match = {'(': ')', '[': ']', '{': '}'}
    
    return is_opening_char(b1) and match[b1] == b2
