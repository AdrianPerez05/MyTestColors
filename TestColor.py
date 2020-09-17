'''
Adrian Perez
9/17/2020
Learning to use color text libraries
'''

from colored import fg, bg, attr
import colored
from colored import stylize
color = fg('#C0C0C0') + bg('#00005f')
res = attr('reset')

print (color + "|\---/|" + res)
print (color + "| o_o |" + res)
print (color + " \_^_/" + res)

print (color + " /\_/\ " + res)
print (color + "( o.o )" + res)
print (color + " > ^ < " + res)



