import pandas as pd
import csv

rows = []

df = pd.read_csv('project130_2.csv')


radius = df['planet_radius'].to_list()
mass = df['planet_mass'].to_list()
gravity = []

def conversion(radius, mass):
    for i in range(0, len(radius) - 1):
        try:
            Radius = float(radius[i])
            Mass = float(mass[i])
            radius[i] = Radius * 6.957e+8
            mass[i] = Mass * 1.989e+30
        except Exception as err:
            radius[i] = 0
            mass[i] = 0
            continue

conversion(radius, mass)

def calculateGravity(radius, mass):
    G = 6.674e-11 
    for i in range(0, len(mass)):
        try:
            g = (mass[i] * G) / radius[i]**2 
            gravity.append(g)
        except Exception as err:
            gravity.append(0)
            continue

calculateGravity(radius, mass)
df['gravity'] = gravity

df.to_csv('project131_2.csv')