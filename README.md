# Parse Molecule

https://gist.github.com/antoinehng/506ad642c07566176cf9fa1cb599f371

The main goal is to count the number of each atoms in a molecule. 

The input is a String, and the function returns a dictionary. 

It needs pyhon3 to work.

## How to run 
To run the program with basic examples : 


`python3 main.py`

You can run the program with one or more molecules as an argument

`python3 main.py H2O C4H12O6`

You can run tests using 

`python3 tests.py`

You can import parse_molecule in your own program with
```
from parser import parse_molecule

parse_molecule(H2O)
```


