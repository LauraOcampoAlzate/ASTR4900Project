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
N = 500 #Number of data points and images for the animation
theta = np.linspace(0, 2*np.pi, N)

#These are the values for the semi-major axis and eccentricity
#The list follows Mercury, Venus, Earth, Mars, and Jupiter last
SMMerc = 0.4 #AU
EccMerc = 0.205
SMV = 0.7 #AU
EccV = 0.007
SME = 1 #AU
EccE = 0.017
SMMars = 1.5 #AU
EccMars = 0.094
SMJ = 5.2 #AU

#Limits the input for the eccentricity
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

#Plugging in the values for the inner planets and Jupiter
MercR = EOQ(SMMerc, EccMerc, theta)
VenusR = EOQ(SMV, EccV, theta)
EarthR = EOQ(SME, EccE, theta)
MarsR = EOQ(SMMars, EccMars, theta)
JupiterR = EOQ(SMJ, EccJ, theta)

#Changing polar coordinates to cartesian
MeXCoord = MercR * np.sin(theta)
MeYCoord = MercR * np.cos(theta)
VXCoord = VenusR * np.sin(theta)
VYCoord = VenusR * np.cos(theta)
EXCoord = EarthR * np.sin(theta)
EYCoord = EarthR * np.cos(theta)
MaXCoord = MarsR * np.sin(theta)
MaYCoord = MarsR * np.cos(theta)
JXCoord = JupiterR * np.sin(theta)
JYCoord = JupiterR * np.cos(theta)

#This plots the final orbits
plt.figure()
plt.style.use('dark_background')
plt.plot(0, 0, "*", color="gold", ms=10)
plt.plot(MeXCoord, MeYCoord, 'o', color="lightgrey", ms=1)
plt.plot(VXCoord, VYCoord, 'o', color="crimson", ms=1)
plt.plot(EXCoord, EYCoord, 'o', color="forestgreen", ms=1)
plt.plot(MaXCoord, MaYCoord, 'o', color="lightsalmon", ms=1)
plt.plot(JXCoord, JYCoord, 'o', color="orange", ms=1)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.title("Inner Planets' Orbit" +
          " Jupiter's Orbit with Eccentricity " + str(EccJ))
plt.xlabel('x')
plt.ylabel('y')

#This is saving the plots to save for an animation
t = np.arange(0, N, 1)
for i in range(len(t)):
    plt.style.use('dark_background')
    plt.plot(0, 0, "*", color="gold", ms=10)
    plt.plot(MeXCoord[i], MeYCoord[i], 'o', color="lightgrey", ms=1)
    plt.plot(VXCoord[i], VYCoord[i], 'o', color="crimson", ms=1)
    plt.plot(EXCoord[i], EYCoord[i], 'o', color="forestgreen", ms=1)
    plt.plot(MaXCoord[i], MaYCoord[i], 'o', color="lightsalmon", ms=1)
    plt.plot(JXCoord[i], JYCoord[i], 'o', color="orange", ms=1)
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.title("Inner Planets' Orbit" +
              " Jupiter's Orbit with Eccentricity " + str(EccJ))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig(f"Frame{i:03d}.png")
    plt.close()
