import math 

#定义一元二次方程函数
def formula(a,b,c):
    def function(x):
        return a*x**2+b*x+c
    return function


#找f(a)*f(b)<0的点函数
def findx(x,y,f):
    i=0
    while f(x+math.exp(i))*y>0:
        i+=1
    return x+math.exp(i)


#求解函数
def solve(a,b,p,f):
    m=(a+b)/2
    while(b-m)>p:
        if f(m)*f(a)>0:
            a=m
        elif f(m)*f(a)==0:
            return m,True
        else:
            b=m
        m=(a+b)/2
        return m,False


#输入a,b,c
a=float(input("a="))
while a==0:
    print("a不能输入为0,请重新输入,a=")
    a=float(input("a="))
b=float(input("b="))
c=float(input("c="))


#定义得到一元二次方程
f=formula(a,b,c)


#驻点
y0=0
x0=(y0-b)/(2*a)


#极值点
x=x0
y0=f(x)


#判断函数是否过x轴
if a*y0<0:
    #p为解得精度
    p=0.0000001
    x=findx(x,y0,f)
    r=solve(x0,x,p,f)


    #判断是否为近似解兵输出
    if r[1]:
        print("此方程式的解为："+str(r[0]) + ", " + str(2*x0 - r[0]))
    else:
        print("此方程式的近似解为："+str(r[0]) + ", " + str(2*x0 - r[0]) )

elif a*y0==0:
    print("此方程式的解为："+str(x0))
else:
    print("此方程式无解！")