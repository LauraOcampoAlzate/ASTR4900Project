#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:45:08 2020

@author: lauraocampo
"""

import numpy as np
import scipy.constants as sc
import matplotlib.pyplot as plt

def EOQ(A, E):
    """This is the Elliptical Orbit Equation (EOQ) where
    we are finding r, the distance from the focus. The equation
    is dependent on A, the semi-major axis, E, the eccentricity, and
    THET, the angle around the orbit. We are also assuming that the orbit
    is at initial angle of 0 degrees."""
    theta = np.linspace(0, 2*np.pi, 1000)

    #Saving Values every 10 degrees
    phi = 0
    for i in range(len(theta)):
        if (phi % 10) == 0 or i == theta[0]:
            R = (A * (1 - E**2)) / (1 + E * np.cos(theta))

    
        plt.figure()
        plt.plot(0, 0, "*")
        plt.plot(EXCoord, EYCoord)

        plt.xlim(-2, 2)
        plt.ylim(-2, 2)
        plt.title("Orbit Simulation")
        plt.xlabel('x')
        plt.ylabel('y')        

        fr = int(phi/20)
        plt.savefig(f"Frame{fr:03d}.png")
        plt.close()  
    
    phi += 1
    return R


def VEL(D, S):
    """This is the Vis-Viva Equation (VEL) where we are finding the
    magnitude of the velocity at any point in the elliptical orbit.
    Here we use G as the gravitational constant, M is the mass of the Sun
    in kilograms, D is distance from the focus, and S is the semi-major
    axis."""

    M = 2 * 10**30 #The mass of the Sun in kg
    V = np.sqrt(sc.G * M * ((2 / D) - (1 / S)))
    return V


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

EarthR = EOQ(SME, EccE)
EarthV = VEL(EarthR, SME)

EXCoord = EarthR * np.sin(theta)
EYCoord = EarthR * np.cos(theta)

