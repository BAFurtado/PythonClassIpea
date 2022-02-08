# BAD
from numpy import *
# GOOD
import numpy as np


y = 'global_variavel'


def define_x():
    y = 'variavel_dentro_funcao'
    print(y)


# print(x)
define_x()
