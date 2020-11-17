#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:45:08 2020

@author: lauraocampo
"""

import numpy as np
import matplotlib.pyplot as plt


def EOQ(A, E, THET):
    """This is the Elliptical Orbit Equation (EOQ) where
    we are finding r, the distance from the focus. The equation
    is dependent on A, the semi-major axis, E, the eccentricity, and
    THET, the angle around the orbit. We are also assuming that the orbit
    is at initial angle of 0 degrees."""
    R = (A * (1 - E**2)) / (1 + E * np.cos(THET))    
    return R


#Initial Conditions
theta = np.linspace(0, 2*np.pi, 500)
SME = 1 #in AU
SMJ = 5.2 #in AU
while True:
    try:
        EccE = float(input("What would you like for Earth's eccentricity?"))
    except ValueError:
        print("Please pick a number between 0 and 1")
        continue
    if EccE < 0.0 and EccE > 1.0:
        print("Please pick a number between 0 and 1")
        continue
    break

while True:
    try:
        EccJ = float(input("What would you like for Jupiter's eccentricity?"))
    except ValueError:
        print("Please pick a number between 0 and 1")
        continue
    if EccE < 0.0 and EccE > 1.0:
        print("Please pick a number between 0 and 1")
        continue
    break

EarthR = EOQ(SME, EccE, theta)
JupiterR = EOQ(SMJ, EccJ, theta)
EXCoord = EarthR * np.sin(theta)
EYCoord = EarthR * np.cos(theta)
JXCoord = JupiterR * np.sin(theta)
JYCoord = JupiterR * np.cos(theta)

t = np.arange(0, 500, 1)
for i in range(len(t)):
    EXCoord = EarthR * np.sin(theta)
    EYCoord = EarthR * np.cos(theta)
    JXCoord = JupiterR * np.sin(theta)
    JYCoord = JupiterR * np.cos(theta)
    plt.style.use('dark_background')
    plt.plot(0, 0, "*", color="gold", ms=10)
    plt.plot(EXCoord[i], EYCoord[i], 'o', color="forestgreen", ms=1)
    plt.plot(JXCoord[i], JYCoord[i], 'o', color="orange", ms=5)
    plt.xlim(-6, 6)
    plt.ylim(-6, 6)
    plt.title("Earth's Orbit with Eccentricity " + str(EccE) +
              " Jupiter's Orbit with Eccentricity " + str(EccJ))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f"Frame{i:03d}.png")
    plt.close()
