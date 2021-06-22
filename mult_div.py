# mult_div.py - some existing python code that does something

import sys

def mult_div(arg1, arg2):
    """Return the product and division of the two arguments"""
    return arg1*arg2, arg1/arg2

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    # Command line argument
    if len(sys.argv) != 3:
        print(f'Usage: {sys.argv[0]} <arg1> <arg2>')
        exit(-1)
    arg1 = int(sys.argv[1])
    arg2 = int(sys.argv[2])

    mult, div = mult_div(arg1, arg2)

    print(f'mult={mult}, div={div}')
