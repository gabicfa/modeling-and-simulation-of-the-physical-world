# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:47:32 2015

@author: gabialmeida
"""

import matplotlib.pyplot as plt
from pylab import *
from funcs import *

def calcPopulation (gamaT, T, P, betaR, Tc, V, alfaV, Rc, time):
    
    Ti=[0]*time
    Ri=[0]*time
    Vi=[0]*time
    Ti[0]= T
    Ri[0]= R
    Vi[0]= V
    f=1.9

    for i in range(1,time):
        DT = CalcDeltaT(gamaT, Ti[i-1], f, P)
        Ti[i] = Ti[i-1] + DT
         
        DR = CalcDeltaR(Ri[i-1], betaR, Ti[i-1], Tc)
        Ri[i] = Ri[i-1] + DR
        
        DV = CalcDeltaV(Vi[i-1], alfaV, Ri[i-1], Rc)
        Vi[i]= Vi[i-1] + DV
        
    print(Ti[time-1])
    print(Ri[time-1])
    print(Vi[time-1])
   
    Time = range(0, time)  
    
    plt.plot(Time, Ti, 'b-')
    plt.axis([0, time-1, 9000000, 30000000])
    plt.xlabel('time [anos]')
    plt.ylabel('T[population of sharks]')
    plt.title('Population of Sharks')
    plt.show()
    
    
    plt.plot(Time, Ri, 'g-')
    plt.axis([0, time-1, 15000000, 50000000])
    plt.xlabel('time [anos]')
    plt.ylabel('R[population of rays]')
    plt.title('Population of Rays')
    plt.show()
    
    
    plt.plot(Time, Vi, 'r-')
    plt.axis([0, time-1, 70000000, 160000000])
    plt.xlabel('time [anos]')
    plt.ylabel('V[population of scallops]')
    plt.title('Population of Scallops')
    plt.show()
    
    plt.plot()
    
gamaT=0.06

T= 10000000 
R= 20000000 
P= 700000

betaR=0.08
Tc=12000000

V= 80000000 
alfaV=0.1
Rc=23000000
time= 30 

    
calcPopulation (gamaT, T, P, betaR, Tc, V, alfaV, Rc, time)
