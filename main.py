
import utils

class FormulaParser(object):
    bracesStack = []
    countStacks = [{}]
    index = 0

    def isClosingChar(self, char):
        closingBraces = [')', ']', '}']
        return char in closingBraces and char

    def isOpeningChar(self, char):
        closingBraces = ['(', '[', '{']
        return char in closingBraces and char

    def areBracesMatching(self, b1, b2):
        match = {'(': ')', '[': ']', '{': '}'}
        return isOpeningChar(b1) and match[b1] == b2

    def getNextAtom(self, molecule, index):
        # first char should always be an uppercase letter so we check the second one
        i = index
        index += 1
        length = len(molecule)
        if index < length and molecule[index].islower():
            index += 1

        atom = molecule[i: index]
        number = utils.getNextNumber(molecule, index)

        atomLength = len(atom)
        
        if number: atomLength += len(number)
        else: number = 1

        return {'name': atom, 'count': int(number), 'length': atomLength }

    def parse_molecule(self, molecule):
        i = 0
        length = len(molecule)
        while i < length:
            if self.isOpeningChar(molecule[i]):
                i += 1
                self.countStacks.append({})

            elif self.isClosingChar(molecule[i]):
                i += 1
                number = utils.getNextNumber(molecule, i)
                lastLevel = self.countStacks.pop()
                
                if number: 
                    i += len(number)
                    number = int(number)
                else: number = 1

                for atom in lastLevel:
                    if not atom in self.countStacks[-1]:
                        self.countStacks[-1][atom] = 0
                    self.countStacks[-1][atom] += (number * lastLevel[atom])

            else:
                atom = self.getNextAtom(molecule, i)
                i += atom['length']
                if not atom['name'] in self.countStacks[-1]:
                    self.countStacks[-1][atom['name']] = 0

                self.countStacks[-1][atom['name']] += atom['count']


        return self.countStacks[0]


a = FormulaParser()
print(a.parse_molecule('K4[ON(SO3)2]2'))