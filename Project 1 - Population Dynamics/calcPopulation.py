# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 21:47:32 2015

@author: gabialmeida
"""

import matplotlib.pyplot as plt
from pylab import *
from funcs import *

def calcPopulation (gamaT, T, P, betaR, Tc, V, alfaV, Rc, tempo):
    
    Ti=[0]*tempo
    Ri=[0]*tempo
    Vi=[0]*tempo
    Ti[0]= T
    Ri[0]= R
    Vi[0]= V
    f=1.9

    for i in range(1,tempo):
        DT = CalcDeltaT(gamaT, Ti[i-1], f, P)
        Ti[i] = Ti[i-1] + DT
         
        DR = CalcDeltaR(Ri[i-1], betaR, Ti[i-1], Tc)
        Ri[i] = Ri[i-1] + DR
        
        DV = CalcDeltaV(Vi[i-1], alfaV, Ri[i-1], Rc)
        Vi[i]= Vi[i-1] + DV
        
    print(Ti[tempo-1])
    print(Ri[tempo-1])
    print(Vi[tempo-1])
   
    Tempo = range(0, tempo)  
    
    plt.plot(Tempo, Ti, 'b-')
    plt.axis([0, tempo-1, 9000000, 30000000])
    plt.xlabel('tempo [anos]')
    plt.ylabel('T[populacao de tubaroes]')
    plt.title('Populacao de Tubarao')
    plt.show()
    
    
    plt.plot(Tempo, Ri, 'g-')
    plt.axis([0, tempo-1, 15000000, 50000000])
    plt.xlabel('tempo [anos]')
    plt.ylabel('R[populacao de raias]')
    plt.title('Populacao de Rais')
    plt.show()
    
    
    plt.plot(Tempo, Vi, 'r-')
    plt.axis([0, tempo-1, 70000000, 160000000])
    plt.xlabel('tempo [anos]')
    plt.ylabel('V[populacao de vieiras]')
    plt.title('Populacao de vieiras')
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
tempo= 30 

    
calcPopulation (gamaT, T, P, betaR, Tc, V, alfaV, Rc, tempo)
