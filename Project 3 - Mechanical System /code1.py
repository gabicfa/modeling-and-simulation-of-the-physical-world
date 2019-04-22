# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:16:36 2015

@author: gabialmeida
"""
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
from math import sin,cos

def func(L,T):
    AR = (mi_e*m*10*L[1])/(((L[0]**2)+((L[1]*c)**2))**(1/2))
    ARr = L[1]*c/(L[0]**2+(L[1]*c)**2)**(1/2)
    AF = ((m*L[0]**2)/R) - ARr
    dwdt = ((AF)*b - (AR*c))/I
    dvdt = (-(mi_d*m*10*L[0])/((L[0]**2)+((L[1]*c)**2))**(1/2))/m
    dodt = L[0]/R
    dxxdt = L[0]*sin(L[2])/2
    dxydt = L[0]*cos(L[2])
    dkdt = L[1]
    #angulofinal=dodt+dkdt
    return [dvdt,dwdt,dodt,dxxdt,dxydt,dkdt]

V= linspace(10,25,16)
listaangulosfinais=[]
m = 850 #Kg
mi_d = 0.65 #Mi Cinético
mi_e = 0.95
W0 = 0 #Velocidade Angular Inicial
DX0 = 0 #Posição Inicial X
DY0 = 0 #Posiçao Inicial Y
O0 = 0 #ângulo inicial --> Curva
K0 = 0 #ângulo inicial --> Carro
b = 1.5 #Comprimento Frente
c = 2 #Comprimento Traseira
R = 10

'''Momento de Inércia Real'''
#I = m*(2+1.5)/12

'''Momento de Inércia Falso'''
I = 27.42*m*(2+1.5)
T = linspace(0,9,1001)

for velocidade in V :

    V0 = velocidade #Velocidade Linear Inicial
    L = [V0,W0,O0,DX0,DY0,K0]

    Z = odeint(func,L,T)
    for linha in range(0,1001):
        if (Z[linha][0])<0.001:
            angulofinal=(Z[linha][2])+(Z[linha][5])
            break
    listaangulosfinais.append(angulofinal)
        
plt.plot(V,listaangulosfinais,'r')
plt.axis([10, 25, 0, 11])
plt.ylabel('angulo final(rad)')
plt.xlabel('velocidade inicial(m/s)')
plt.title("Angulo Final em funcao da velocidade inicial")



    
    