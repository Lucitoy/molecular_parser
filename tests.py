import utils
import parser
import unittest


class TestUtils(unittest.TestCase):
    def test_isClosingChar_true(self):
        closingChars = [')', ']', '}']

        for char in closingChars:
            self.assertTrue(utils.isClosingChar(char))

    def test_isClosingChar_false(self):
        nonClosingChars = ['p', 'hola', '$', '(', ':']
        for char in nonClosingChars:
            self.assertFalse(utils.isClosingChar(char))

    def test_isOpeningChar_true(self):
        openingChar = ['(', '[', '{']

        for char in openingChar:
            self.assertTrue(utils.isOpeningChar(char))

    def test_isOpeningChar_false(self):
        nonOpeningChars = ['p', 'bonjour pedro', '$', ')', ':']
        for char in nonOpeningChars:
            self.assertFalse(utils.isOpeningChar(char))

    def test_areBracesMatching_true(self):
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        for i in range(len(opening)):
            self.assertTrue(utils.areBracesMatching(opening[i], closing[i]))

    def test_areBracesMatching_false(self):
        opening = ['(', '(', '(', '[', '[', ' [', '{', '{', '{', ']']
        closing = [']', '}', '4', ')', '}', '/', ')', ']', 'h', '[']

        for i in range(len(opening)):
            self.assertFalse(utils.areBracesMatching(opening[i], closing[i]))


class TestParser(unittest.TestCase):
    def test_getNextNumber(self):
        data = ["3333A", "1", "a", ")"]
        expected = ["3333", "1", False, False]

        for i in range(len(data)):
            self.assertEqual(parser.getNextNumber(data[i], 0), expected[i])

    def test_getNextNumber_with_different_index(self):
        data = "Ke12"
        expected = "12"
        index = 2
        self.assertEqual(parser.getNextNumber(data, index), expected)

    def test_getNextAtom(self):
        data = 'H2O'
        index = 0
        expected = {'name': 'H', 'count': 2, "length": 2}
        self.assertEqual(parser.getNextAtom(data, index), expected)

    def test_getNextAtom_no_number(self):
        data = 'HO'
        index = 0
        expected = {'name': 'H', 'count': 1, "length": 1}
        self.assertEqual(parser.getNextAtom(data, index), expected)

    def test_getNextAtom_with_lower(self):
        data = 'HeC'
        index = 0
        expected = {'name': 'He', 'count': 1, "length": 2}
        self.assertEqual(parser.getNextAtom(data, index), expected)

    def test_getNextAtom_with_different_index(self):
        data = 'HeC'
        index = 2
        expected = {'name': 'C', 'count': 1, "length": 1}
        self.assertEqual(parser.getNextAtom(data, index), expected)

    def test_parse_molecule_simple(self):
        data = 'HeC'
        expected = {'He': 1, 'C': 1}
        self.assertEqual(parser.parse_molecule(data), expected)

    def test_parse_molecule_nested(self):
        data = [
            '',
            'Mg(OH)2',
            'K4[ON(SO3)2]2',
            "CH2OHCHOHCH2OH",
            "U3Br12{P2[ONHe9({SO}3)2]2}9"
        ]
        expected = [
            {},
            {'Mg': 1, 'O': 2, 'H': 2},
            {'K': 4, 'O': 14, 'N': 2, 'S': 4},
            {'C': 3, 'H': 8, 'O': 3},
            {'U': 3, 'Br': 12, 'P': 18, 'O': 126, 'N': 18, 'He': 162, 'S': 108}
        ]

    def test_parse_molecule_invalid_formula(self):
        data = "U3Br1}2{P2[ONHe9({SO}3)2]2}9"
        
        with self.assertRaises(Exception) as context:
            parser.parse_molecule(data)
            
            self.assertTrue('Invalid formula' in context.exception)


if __name__ == '__main__':
    unittest.main()
