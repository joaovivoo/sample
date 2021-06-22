# arith.py - arithmétique

import sys

def somme(n1, n2, n3):
    """Return the sum of the three arguments"""
    return n1 + n2 + n3
        
#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) != 4:
        print(f'Usage: {sys.argv[0]} <n1> <n2> <n3>')
        exit(-1)
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    
    res = somme(n1, n2, n3)

    print(f'somme={res}')
