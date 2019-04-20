# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 07:47:13 2015

@author: gabialmeida
"""

def CalcDeltaT (gamaT, T, f, P):
    return (gamaT*T*f)-P

def CalcDeltaR (R, betaR, T, Tc):
    return betaR*R*(1-(T/Tc))

def CalcDeltaV (V, alfaV, R, Rc):
    return alfaV*V*(1-(R/Rc))