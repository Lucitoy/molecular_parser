import utils
import parser
import unittest


class TestUtils(unittest.TestCase):
    def test_is_closing_char_true(self):
        closing_chars = [')', ']', '}']

        for char in closing_chars:
            self.assertTrue(utils.is_closing_char(char))

    def test_is_closing_char_false(self):
        non_closing_chars = ['p', 'hola', '$', '(', ':']
        for char in non_closing_chars:
            self.assertFalse(utils.is_closing_char(char))

    def test_is_opening_char_true(self):
        opening_char = ['(', '[', '{']

        for char in opening_char:
            self.assertTrue(utils.is_opening_char(char))

    def test_is_opening_char_false(self):
        non_opening_chars = ['p', 'bonjour pedro', '$', ')', ':']
        for char in non_opening_chars:
            self.assertFalse(utils.is_opening_char(char))

    def test_are_brackets_matching_true(self):
        opening = ['(', '[', '{']
        closing = [')', ']', '}']

        for i in range(len(opening)):
            self.assertTrue(utils.are_brackets_matching(opening[i], closing[i]))

    def test_are_brackets_matching_false(self):
        opening = ['(', '(', '(', '[', '[', ' [', '{', '{', '{', ']']
        closing = [']', '}', '4', ')', '}', '/', ')', ']', 'h', '[']

        for i in range(len(opening)):
            self.assertFalse(utils.are_brackets_matching(opening[i], closing[i]))


class TestParser(unittest.TestCase):
    def test_get_next_number(self):
        data = ['3333A', '1', 'a', ')']
        expected = ['3333', '1', False, False]

        for i in range(len(data)):
            self.assertEqual(parser.get_next_number(data[i], 0), expected[i])

    def test_get_next_number_with_different_index(self):
        data = 'Ke12'
        expected = '12'
        index = 2
        self.assertEqual(parser.get_next_number(data, index), expected)

    def test_get_next_atom(self):
        data = 'H2O'
        index = 0
        expected = {'name': 'H', 'count': 2, 'length': 2}
        self.assertEqual(parser.get_next_atom(data, index), expected)

    def test_get_next_atom_no_number(self):
        data = 'HO'
        index = 0
        expected = {'name': 'H', 'count': 1, 'length': 1}
        self.assertEqual(parser.get_next_atom(data, index), expected)

    def test_get_next_atom_with_lower(self):
        data = 'HeC'
        index = 0
        expected = {'name': 'He', 'count': 1, 'length': 2}
        self.assertEqual(parser.get_next_atom(data, index), expected)

    def test_get_next_atom_with_different_index(self):
        data = 'HeC'
        index = 2
        expected = {'name': 'C', 'count': 1, 'length': 1}
        self.assertEqual(parser.get_next_atom(data, index), expected)

    def test_parse_molecule_simple(self):
        data = 'HeC'
        expected = {'He': 1, 'C': 1}
        self.assertEqual(parser.parse_molecule(data), expected)

    def test_parse_molecule_nested(self):
        data = [
            '',
            'Mg(OH)2',
            'K4[ON(SO3)2]2',
            'CH2OHCHOHCH2OH',
            'U3Br12{P2[ONHe9({SO}3)2]2}9'
        ]
        expected = [
            {},
            {'Mg': 1, 'O': 2, 'H': 2},
            {'K': 4, 'O': 14, 'N': 2, 'S': 4},
            {'C': 3, 'H': 8, 'O': 3},
            {'U': 3, 'Br': 12, 'P': 18, 'O': 126, 'N': 18, 'He': 162, 'S': 108}
        ]

    def test_parse_molecule_invalid_formula(self):
        data = 'U3Br1}2{P2[ONHe9({SO}3)2]2}9'
        
        with self.assertRaises(Exception) as context:
            parser.parse_molecule(data)
            
            self.assertTrue('Invalid formula' in str(context.exception))


if __name__ == '__main__':
    unittest.main()
