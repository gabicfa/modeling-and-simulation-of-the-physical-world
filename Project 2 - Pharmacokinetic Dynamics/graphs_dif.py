# -*- coding: utf-8 -*-
"""
Created on Tue May  5 08:12:04 2015

@author: gabialmeida
"""
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace

t=200
T= range(0, t)

Io=44.4
ki=0.035
ks=1/5
So=0 
Yo=[Io,So]
IoLista= linspace(22.2,88.8,200)

def funcDif(Yt, t):
    dIdt= (-0.4*ki*Yt[0])-(0.6*ki*Yt[0])
    dSdt=(0.4*ki*Yt[0])-(ks*Yt[1])
    return dIdt, dSdt

def calculaConcentracao(Io,T):
    Yo = [Io,So] #de onde vem E0? e C0? 
    # Realiza  a integração numérica
    Y = odeint(funcDif,Yo,T)
    return Y[:,1]

def determinaTempoMenorX(Y,T,x):
    a = 0
    parar = 0
    l = len(Y)
    while parar == 0 and a < l-1: #n-1 para size da lista
        if (Y[a+1] < x and Y[a] >= x):
            parar = 1
        a = a + 1
    if (a == l-1):
        a = 0
    return T[a]

def calculaTempoMenorX(IoLista,T,x):
    n = len(IoLista)
    TMenorQueXLista = n*[0]
    for a, Io in enumerate(IoLista):
        Y = calculaConcentracao(Io,T)        
        TMenorQueXLista[a] = determinaTempoMenorX(Y,T,x)
    return TMenorQueXLista

Y = odeint(funcDif,Yo,T)
print(Y)

plt.plot(T, Y[:,0], 'r-')
plt.plot(T, Y[:,1], 'g-')
plt.axis([0, t-1, -0.5, 45])
plt.xlabel('Tempo')
plt.ylabel('Concentracao (mg/L)')
plt.title('Concentracao de Talidomida no Sangue e no Intestino em Funcao do Tempo')
plt.plot(T, Y[:,0], 'r-', label='concentracao no estomago')
plt.plot(T, Y[:,1], 'g-', label= 'concentracao no sangue')
plt.legend(loc="upper right")
plt.show()

plt.plot(T, Y[:,0], 'r-')
plt.axis([0, t-1, -0.5, 45])
plt.xlabel('Tempo[horas]')
plt.ylabel('Concentracao (mg/L)')
plt.title('Concentracao de Talidomida no Intestino em Funcao do Tempo')
plt.show()

plt.plot(T, Y[:,1], 'g-')
plt.axis([0, t-1, -0.2, 3.5])
plt.xlabel('Tempo[horas]')
plt.ylabel('Concentracao (mg/L)')
plt.title('Concentracao de Talidomida no Sangue em Funcao do Tempo')
plt.show()

fig, ax1= plt.subplots() 
ax1.plot(T, Y[:,1], 'g-')
ax1.set_xlim([0,300])
ax1.set_ylabel('Concentracao de Talidomina no Sangue (mg/L)', color='g')
ax1.set_ylim(-0.5, 3.5)
ax1.set_xlabel('Tempo [horas]')
for tl in ax1.get_yticklabels():
    tl.set_color('g')
        
ax2= ax1.twinx()
ax2.plot(T, Y[:,0],'r-')
ax2.set_ylabel('Concentracao de Talidomida no Intestino (mg/L)', color='r')
ax2.set_ylim(-0.5, 45)
for tl in ax2.get_yticklabels():
    tl.set_color('r')
plt.show()

T = linspace(0,1000,1001) 
TMenorQueXLista = calculaTempoMenorX(IoLista,T,0.018)       
print(TMenorQueXLista)

plt.plot(IoLista,TMenorQueXLista,'b-')
plt.axis([22.2, max(IoLista), 130, 180])
plt.ylabel('Tempo (h) para a Concentração de Talidomida Ficar Menor que a Segura')
plt.xlabel('Concentracao Inicial no Intestino[mg/L]')
plt.show() 