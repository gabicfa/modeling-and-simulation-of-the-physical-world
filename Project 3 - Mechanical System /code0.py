
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
from math import pi,sin,cos

#Parametros 
m = 850 #Kg
mi_d = 0.65 #Mi Cinético
mi_e = 0.95
V0 = 20 #Velocidade Linear Inicial
W0 = 0 #Velocidade Angular Inicial
DX0 = 0 #Posição Inicial X
DY0 = 0 #Posiçao Inicial Y
O0 = 0 #ângulo inicial --> Curva
K0 = 0 #ângulo inicial --> Carro
L = [V0,W0,O0,DX0,DY0,K0]
b = 1.5 #Comprimento Frente
c = 2 #Comprimento Traseira
R = 10
'''Momento de Inércia Real'''
#I = m*(2+1.5)/12
'''Momento de Inércia Falso'''
I = 27.42*m*(2+1.5)

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
	return [dvdt,dwdt,dodt,dxxdt,dxydt,dkdt]

lista_pontos_carrox = []
lista_pontos_carroy = []
lista_angulos_carros1 = []
lista_angulos_carros2 = []

T = linspace(0,9,1001)
Z = odeint(func,L,T)
for i in range (11):
	lista_pontos_carrox.append(Z[i*100,3])
	lista_pontos_carroy.append(Z[i*100,4])
	lista_angulos_carros1.append(Z[i*100,5])
	lista_angulos_carros2.append(Z[i*100,2])

print(lista_angulos_carros1)

print(Z[:,4])
plt.axis([-0.5,10.5,-1,10.5])
plt.axis([0,4,0,11])
plt.plot(Z[:,3],Z[:,4],'r',label='Deslocamento')
plt.plot(T,Z[:,5],'g',label='Deslocamento Angular Curva')
plt.plot(T,Z[:,2],'r',label='Deslocamento Angular Carro')
plt.plot(lista_pontos_carrox,lista_pontos_carroy,'go',)
plt.legend(loc = 'upper left')
plt.show()