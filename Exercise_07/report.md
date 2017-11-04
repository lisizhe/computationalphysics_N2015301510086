# Report: Calculate Poincare sections
### 作者： 李思哲
***
## 题目摘要
Calculate Poincare sections for the pendulum as it undergoes the period-doubling route to chaos. Plot ω versus θ, with one point plotted for each 
drive cycle, as in figure 3.9. Do this for FD=1.4, 1.44, and 1.465, using the other parameters as given in connection with figure 3.10.

## 算法设计
为了画出Poincare sections，需要解决如下两个问题：

* 如何计算出随时间演化的ω和θ数组

* 如何按照题目中的要求，筛选出符合要求的点

对于第一个问题，我们只需要重复上一次作业中的E-C算法便可以解决。而对于第二个问题，则需要合理地选择判断条件。等间隔取点不是一个好主意，所以我尝试了比较差值的方法。
具体来说，就是：

```
if ((OMGD*t[i+1])/(2*math.pi)-int((OMGD*t[i+1])/(2*math.pi))<(OMGD*T)/(2*math.pi)):
```
这个方法可以保证取到的点始终具有较小的误差。
## 核心代码段
```
for i in range(0,LIM-1):
        ω[i+1]=ω[i]-((g/L)*math.sin(θ[i])+Q*ω[i]-FD*math.sin(OMGD*t[i]))*T
        θ[i+1]=θ[i]+ω[i+1]*T
        if θ[i+1]<-math.pi:
            θ[i+1]=θ[i+1]+2*math.pi
        elif θ[i+1]>math.pi:
            θ[i+1]=θ[i+1]-2*math.pi
        else:
            θ[i+1]=θ[i+1]    
        t[i+1]=t[i]+T
        if ((OMGD*t[i+1])/(2*math.pi)-int((OMGD*t[i+1])/(2*math.pi))<(OMGD*T)/(2*math.pi)):
            D.append(θ[i+1])
            W.append(ω[i+1])
```

通过循环生成数据，然后在循环中筛选数据并存入列表中。

## 运行结果
![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1.png)

![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1-1.png)

![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1-2.png)

我们可以看出一些周期倍增的趋势……可是图中依然有一些凌乱的点。

## 一些改良
怎么办呢？我们采用如下方法：

* 只记录300个周期之后的点

追加判断条件：

```
if (t[i+1]>900*math.pi)
```

效果非常明显：

![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1-5.png)

![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1-4.png)

![](https://github.com/lisizhe/computationalphysics_N2015301510086/blob/master/Exercise_07/Figure_1-6.png)

可以清晰地观察到周期倍增的现象。

## 参考资料：

* [1]《计算物理》 by N.J.Giordano
* [[2] Cathaya Liu的repositories](https://github.com/Cathayaliu/computationalphysics_N2015301020026/blob/master/6th%20homework/report.md)

