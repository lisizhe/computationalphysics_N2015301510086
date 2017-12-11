import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


the_origin_V=[[0 for col in range(25)] for row in range(25)]
for i in range(8,16):
    for j in range(8,16):
        the_origin_V[i][j]=1
        #the_origin_V[16][i]=-1
'''
the_origin_V[0][1]=0.67
the_origin_V[6][1]=0.67
the_origin_V[0][5]=0.67
the_origin_V[6][5]=0.67
the_origin_V[0][2]=0.33
the_origin_V[6][2]=0.33
the_origin_V[0][4]=0.33
the_origin_V[6][4]=0.33
'''
    
V=[the_origin_V]

for i in range(0,80):
    VO=V[i]
    K=[[0 for col in range(25)] for row in range(25)]
    Delta_V=0
    for i in range(1,24):
        for j in range(1,24):
            if (VO[i][j]!=1 and VO[i][j]!=-1):
                K[i][j]=round((VO[i-1][j]+VO[i+1][j]+VO[i][j-1]+VO[i][j+1])/4,2)  
                Delta_V+=abs(VO[i][j]-K[i][j])
    for i in range(0,25):
        for j in range(0,25):
            K[i][j]=K[i][j]+V[0][i][j]
    V.append(K)
Ex=[[0 for col in range(25)] for row in range(25)]
Ey=[[0 for col in range(25)] for row in range(25)]
for i in range(1,24):
        for j in range(1,24):
            if (V[80][i][j]!=1 and V[80][i][j]!=-1):
                Ex[i][j]=round((V[80][i-1][j]-V[80][i+1][j])/2,4)
                Ey[i][j]=round((V[80][i][j-1]-V[80][i][j+1])/2,4)
x=[]
for i in range(0,25):
    x.append(i)

y=[]
for i in range(0,25):
    y.append(i)
    
Z1=sum(V[14],[])
Z5=sum(V[15],[])




plt.quiver(y,x,Ey,Ex,minlength=1)

#plt.contour(y,x,V[80],(-1,-0.9,-0.8,-0.7,-0.6,-0.5,-0.4,-0.3,-0.2,-0.1,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1))


plt.show()