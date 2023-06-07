#!/usr/bin/pyhon3
def magic_calculation(a, b, c):
    if a > b:
        return a - b
    elif a < b:
        return (a + b) / c
    else:
        return (a * b) % c
