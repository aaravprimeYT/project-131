import csv
import pandas as pd


df = pd.read_csv("project130_2.csv")



radius = df["planet_radius"].tolist()
mass = df["planet_mass"].tolist()

def convertToSi(radius,mass):
  for i in range(0,len(radius)-1):
    radius[i] = radius[i]*6.957e+8
    mass[i] = mass[i]*1.989e+30

convertToSi(radius,mass)

gravity = []

def gravityCalculation(radius,mass):
  G = 6.674e-11
  for index in range(0,len(mass)):
    g = (mass[index]*G)/((radius[index])**2)
    gravity.append(g)

gravityCalculation(radius,mass)

df["gravity"] = gravity

df.to_csv("project131_2.csv")