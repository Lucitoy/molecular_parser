from parser import parse_molecule

# return {'H': 2, 'O': 1}
water = 'H2O'
print(parse_molecule(water))

# return {'Mg': 1, 'O': 2, 'H': 2}
magnesium_hydroxide = 'Mg(OH)2'
print(parse_molecule(magnesium_hydroxide))

# return {'K': 4, 'O': 14, 'N': 2, 'S': 4}
fremy_salt = 'K4[ON(SO3)2]2'
print(parse_molecule(fremy_salt))

glycerol = "CH2OHCHOHCH2OH"
# return {'C': 3, 'H': 8, 'O': 3}
print(parse_molecule(glycerol))

random_molecule = "U3Br12{P2[ONHe9({SO}3)2]2}9"
print(parse_molecule(random_molecule))

breaking_molecule = "U3Br1}2{P2[ONHe9({SO}3)2]2}9"
print(parse_molecule(breaking_molecule))
