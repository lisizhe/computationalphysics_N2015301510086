# REPORT 1 
### author：lisizhe

***
## 题目表述




## 题目的python实现
```
import matplotlib.pyplot as plt

N1=[0 for x in range(0,101)]
t1=[0 for x in range(0,101)]
N1[0]=0
T1=0.1
t1[0]=0
v=40


for i in range(1,100):
    N1[i]=N1[i-1]+v*T1
    t1[i]=i*T1


plt.title('x-t figure')
plt.xlabel('t/s')
plt.ylabel('x/m')
P1=plt.scatter(t1,N1)

plt.legend(handles = [P1], labels = ['dt=0.1s'], loc = 'best')
plt.show()
```
## 程序运行结果
