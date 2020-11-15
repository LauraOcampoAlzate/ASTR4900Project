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


def VEL(D, S):
    """This is the Vis-Viva Equation (VEL) where we are finding the
    magnitude of the velocity at any point in the elliptical orbit.
    Here we use G as the gravitational constant, M is the mass of the Sun
    in kilograms, D is distance from the focus, and S is the semi-major
    axis."""

    M = 2 * 10**30 #The mass of the Sun in kg
    V = np.sqrt(sc.G * M * ((2 / D) - (1 / S)))
    return V
    