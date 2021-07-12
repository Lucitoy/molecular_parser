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
    atom_length = len(atom)
    if number:
        atom_length += len(number)
    else:
        number = 1

    return {'name': atom, 'count': int(number), 'length': atom_length}


def parse_molecule(molecule):
    """
        @Parameters: molecule: string => the formula of a molecule

        @Returns: dict with the count of each atoms in the molecule

        It stacks dict for each level of brackets and add them 
        in the lower level once a cracket closes
    """
    if not molecule:
        return {}

    i = 0
    brackets_stack = []
    counter_stack = [{}]

    length = len(molecule)
    while i < length:
        if utils.is_opening_char(molecule[i]):
            brackets_stack.append(molecule[i])
            i += 1
            counter_stack.append({})

        elif utils.is_closing_char(molecule[i]):
            # invalid formula protection
            if not len(brackets_stack):
                raise Exception('Invalid formula')
            lastBrace = brackets_stack.pop()
            if not utils.are_brackets_matching(lastBrace, molecule[i]):
                raise Exception('Invalid formula')

            i += 1
            number = get_next_number(molecule, i)
            last_level = counter_stack.pop()

            if number:
                i += len(number)
                number = int(number)
            else:
                number = 1

            for atom in last_level:
                if not atom in counter_stack[-1]:
                    counter_stack[-1][atom] = 0
                counter_stack[-1][atom] += (number * last_level[atom])

        else:
            atom = get_next_atom(molecule, i)
            i += atom['length']
            if not atom['name'] in counter_stack[-1]:
                counter_stack[-1][atom['name']] = 0
            counter_stack[-1][atom['name']] += atom['count']

    if not len(brackets_stack):
        return counter_stack[0]
    else:
        raise Exception('Invalid formula')
