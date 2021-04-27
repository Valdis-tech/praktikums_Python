# -*- coding: utf-8 -*- 
""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
from math import pi

radiuss=float(input("Ievadi rādiusu:"))

garums=2*pi*radiuss

laukums=pi*radiuss*2

print(f'riņķa līnijas garums ir {garums}')

print(f'riņka līnijas laukums ir {laukums}')
