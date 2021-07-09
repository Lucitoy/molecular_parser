def isClosingChar(char):
    closingBraces = [')', ']', '}']
    return char in closingBraces

def isOpeningChar(char):
    closingBraces = ['(', '[', '{']
    return char in closingBraces

def areBracesMatching(b1, b2):
    match = {'(': ')', '[': ']', '{': '}'}
    
    return isOpeningChar(b1) and match[b1] == b2
