# main.py
from calculator.basic import add, subtract, multiply
from calculator.advanced import power, square_root
from calculator.advanced.trigonometry import sin, cos, tan
from calculator import *
#from calculator import basic
import sys
print(sys.path)
print(basic.addition.add(2, 3))         # Вывод: 5 (указать путь при import *)
print(subtract(5, 2))        # Вывод: 3
print(power(2, 3))           # Вывод: 8
print(square_root(16))       # Вывод: 4.0
print(multiply(4, 5))
print(sin(0.5), cos(0.5), tan(1))
