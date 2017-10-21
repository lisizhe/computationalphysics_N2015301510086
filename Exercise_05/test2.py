# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 20:58:58 2017

@author: Dell
"""

import matplotlib.pyplot as plt
import math

def BACKSPIN_BALL(V0,A,U,LIM):
    
    X=[0 for x in range(0,LIM)]
    Y=[0 for x in range(0,LIM)]


    X[0]=0
    Y[0]=1.8


    T=0.01
    g=9.8

    VX=V0*math.cos(A)
    VY=V0*math.sin(A)

    V=V0
    for i in range(1,LIM):
        VX=VX-(0.0039*V*VX)*T
        VY=VY-g*T-(4.1*0.0001*U*VX)*T

        V=(VX*VX+VY*VY)**0.5
        X[i]=X[i-1]+VX*T
        Y[i]=Y[i-1]+VY*T

    
    P1=plt.plot(X,Y)

    
    return P1

BACKSPIN_BALL(15,math.pi/4,33,5001)
BACKSPIN_BALL(15,math.pi/4,-33,5001)
BACKSPIN_BALL(15,math.pi/4,0,5001)

plt.title('Spin and Backspin Baseball')
plt.ylabel('y/m')
plt.xlabel('x/m')
plt.xlim((0,25))
plt.ylim((0,8))

plt.show()
