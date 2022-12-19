from helpers import *


for i in range(8, 26):
    input(yellow(f'WARNING: overwriting from {i} to 25'))
    os.system('cp def.dat ' + str(i) + '.dat')
    os.system('cp def.py ' + str(i) + '.py')