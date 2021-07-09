def getNextNumber(string, index):
    i = index
    while index < len(string) and string[index].isdigit():
        index += 1
    
    if index == i: return False

    return string[i: index]

def isClosingChar(char):
    closingBraces = [')', ']', '}']
    return char in closingBraces and char


def isOpeningChar(char):
    closingBraces = ['(', '[', '{']
    return char in closingBraces and char


def areBracesMatching(b1, b2):
    match = {'(': ')', '[': ']', '{': '}'}
    return isOpeningChar(b1) and match[b1] == b2
