
import utils



bracesStack = []
countStacks = [{}]
index = 0

def isClosingChar(char):
    closingBraces = [')', ']', '}']
    return char in closingBraces and char

def isOpeningChar(char):
    closingBraces = ['(', '[', '{']
    return char in closingBraces and char

def areBracesMatching(b1, b2):
    match = {'(': ')', '[': ']', '{': '}'}
    return isOpeningChar(b1) and match[b1] == b2

def getNextAtom(molecule, index):
    # first char should always be an uppercase letter so we check the second one
    i = index
    index += 1
    length = len(molecule)
    if index < length and molecule[index].islower():
        index += 1

    atom = molecule[i: index]
    number = utils.getNextNumber(molecule, index)

    atomLength = len(atom)

    if number:
        atomLength += len(number)
    else:
        number = 1

    return {'name': atom, 'count': int(number), 'length': atomLength}

def parse_molecule(molecule):
    i = 0
    length = len(molecule)
    while i < length:
        if isOpeningChar(molecule[i]):
            i += 1
            countStacks.append({})

        elif isClosingChar(molecule[i]):
            i += 1
            number = utils.getNextNumber(molecule, i)
            lastLevel = countStacks.pop()

            if number:
                i += len(number)
                number = int(number)
            else:
                number = 1

            for atom in lastLevel:
                if not atom in countStacks[-1]:
                    countStacks[-1][atom] = 0
                countStacks[-1][atom] += (number * lastLevel[atom])

        else:
            atom = getNextAtom(molecule, i)
            i += atom['length']
            if not atom['name'] in countStacks[-1]:
                countStacks[-1][atom['name']] = 0

            countStacks[-1][atom['name']] += atom['count']

    return countStacks[0]



print(parse_molecule('K4[ON(SO3)2]2'))
