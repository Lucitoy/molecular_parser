from parser import parse_molecule
import sys

if len(sys.argv) < 2:
    """
        Default behavior if no arguments given
    """

    water = 'H2O'
    print(parse_molecule(water))

    magnesium_hydroxide = 'Mg(OH)2'
    print(parse_molecule(magnesium_hydroxide))

    fremy_salt = 'K4[ON(SO3)2]2'
    print(parse_molecule(fremy_salt))

    glycerol = 'CH2OHCHOHCH2OH'
    print(parse_molecule(glycerol))

    random_molecule = 'U3Br12{P2[ONHe9({SO}3)2]2}9'
    print(parse_molecule(random_molecule))

    try:
        breaking_molecule = 'U3Br1}2{P2[ONHe9({SO}3)2]2}9'
        print(parse_molecule(breaking_molecule))
    except Exception:
        print('Invalid formula')

else:
    for i in range(1, len(sys.argv)):
        print(parse_molecule(sys.argv[i]))