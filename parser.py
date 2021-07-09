import utils


def get_next_number(string, index):
    """
        Returns the string representing the next number
        you encounter (index must be on the first digit of the number)
        @Parameters: 
            string
        
        @Returns: string or False
    """
    i = index
    while index < len(string) and string[index].isdigit():
        index += 1

    if index == i:
        return False

    return string[i: index]

def get_next_atom(molecule, index):
    """
        @Parameters:
            molecule: string
            index: int
        
        @returns: 
            dict:
                name: string
                count: int
                length: int
    """
    i = index
    # search for i + 1 because first char is always upper
    index += 1

    length = len(molecule)
    if index < length and molecule[index].islower():
        index += 1

    atom = molecule[i: index]
    number = get_next_number(molecule, index)
    atomLength = len(atom)
    if number:
        atomLength += len(number)
    else:
        number = 1

    return {'name': atom, 'count': int(number), 'length': atomLength}


def parse_molecule(molecule):
    """
        @Parameters: molecule: string => the formula of a molecule
        
        @Returns: dict with the count of each atoms in the molecule
    """
    if not molecule: 
        return {}
    
    i = 0
    bracketsStack = []
    counterStack = [{}]

    length = len(molecule)
    while i < length:
        if utils.is_opening_char(molecule[i]):
            bracketsStack.append(molecule[i])
            i += 1
            counterStack.append({})

        elif utils.is_closing_char(molecule[i]):
            # invalid formula protection
            if not len(bracketsStack):
                raise Exception('Invalid formula')
            lastBrace = bracketsStack.pop()
            if not utils.are_brackets_matching(lastBrace, molecule[i]):
                raise Exception('Invalid formula')

            i += 1
            number = get_next_number(molecule, i)
            lastLevel = counterStack.pop()

            if number:
                i += len(number)
                number = int(number)
            else:
                number = 1

            for atom in lastLevel:
                if not atom in counterStack[-1]:
                    counterStack[-1][atom] = 0
                counterStack[-1][atom] += (number * lastLevel[atom])

        else:
            atom = get_next_atom(molecule, i)
            i += atom['length']
            if not atom['name'] in counterStack[-1]:
                counterStack[-1][atom['name']] = 0
            counterStack[-1][atom['name']] += atom['count']

    return counterStack[0]
