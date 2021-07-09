def getNextNumber(string, index):
    i = index
    while index < len(string) and string[index].isdigit():
        index += 1
    
    if index == i: return False
    
    return string[i: index]
