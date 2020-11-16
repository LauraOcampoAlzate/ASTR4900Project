#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:45:08 2020

@author: lauraocampo
"""

import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt


def EOQ(A, E, THET):
    """This is the Elliptical Orbit Equation (EOQ) where
    we are finding r, the distance from the focus. The equation
    is dependent on A, the semi-major axis, E, the eccentricity, and
    THET, the angle around the orbit. We are also assuming that the orbit
    is at initial angle of 0 degrees."""

    R = (A * (1 - E**2)) / (1 + E * np.cos(theta))    
    return R


#Initial Conditions
theta = np.linspace(0, 2*np.pi, 1000)
SME = 1 #in AU
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

EarthR = EOQ(SME, EccE, theta)

t = np.arange(0, 1000, 1)
for i in range(len(t)):
    EXCoord = EarthR[i] * np.sin(theta)
    EYCoord = EarthR[i] * np.cos(theta)

    plt.figure()
    plt.plot(0, 0, "*", color="gold")
    plt.plot(EXCoord[i], EYCoord[i], ".", color="forestgreen")
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)
    plt.title("Orbit Simulation")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f"Frame{i:03d}.png")
    plt.close()
