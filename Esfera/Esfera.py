'''Santana Mares Jasmin Aide GITI9071'''

from math import pi

"""Función que retorna el volumen de la esfera """


def sphere_volume(r: float) -> float:
    return (4 / 3) * (pi * (r ** 3))


""" Función que retorna el área de la esfera """


def sphere_area(r: float) -> float:
    return 4 * pi * (r ** 2)
