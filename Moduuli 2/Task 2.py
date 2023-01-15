"""
Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
"""
import math

Radius = float(input('Anna ympyrän säteen arvo. '))
CircleArea = math.pi * Radius**2.0

print(f"Ympyrän pinta-ala, jonka säde on {Radius} yhtä suuri kuin {CircleArea:.2f}")