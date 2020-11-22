from CoolProp.CoolProp import PropsSI
import math
#圆形管槽内的强制对流换热

#Hyper parameter
#P_Pa_Pressure
#T_K_Temperature;
#D_kg/m^3_Mass density;
#C_J/(kg`k)_比热容
#U_pa`s_动力粘度
#V_m^2/s_运动粘度
#λ_W/(m`L)_导热系数

#Pr


p = 101325
def para(p,t):
    D=PropsSI('D', 'P', p, 'T', t, 'Water')
    C = PropsSI('C', 'P', p, 'T', t, 'Water')
    V = PropsSI('V', 'P', p, 'T', t, 'Water')*0.001
    λ = PropsSI('L', 'P', p, 'T', t, 'Water')
    Pr=PropsSI('Prandtl', 'P', p, 'T', t, 'Water')
    return [D,C,V,λ,Pr]

#U=D`V
#a=V/Pr

def Re(v,d,V):
    re=v*d/V
    return  re

def Nu(Re,Pr,l,d,tf,tw,p):
    if Pr>0.6:
        if Re <2300 and Pr >=0.48 and Pr <=16700:
            if (para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2])>=0.0044 and (para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2]) <=9.75 and pow(Re*Pr*d/l,1/3)*pow((para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2]),0.14)>=2:
                nu=1.86*pow(Re*Pr*d/l,1/3)*pow((para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2]),0.14)
                print('Sieder-Tade公式',nu)
                return nu
            else:
                print('error',Pr,(para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2]),pow(Re*Pr*d/l,1/3)*pow((para(p,tf)[0]*para(p,tf)[2])/(para(p,tw)[0]*para(p,tw)[2]),0.14))
                pass

        elif Re>=10000 and Re <=120000 and Pr >=0.7 and Pr<=120 and l/d>=10:
            if tw >tf:
                nu=0.023*pow(Re,0.8)*pow(Pr,0.4)
                print('Dittus-Boelter公式(加热流体)： ',nu)
                return nu
            else:
                nu=0.023*pow(Re,0.8)*pow(Pr,0,3)
                print('Dittus-Boelter公式（冷却流体）： ', nu)
                return nu
        elif Re>=2300 and Re <=1000000 and Pr >=0.6 and Pr<=100000 :
            f=pow(1.8*math.log10(Re)-1.5,-2)
            nu=(1+pow(d/l,2/3))*(f*Pr*(Re-1000)/8)/(1+12.7*(pow(Pr,2/3)-1)*pow(f/8,1/2))
            print('Gnielinski公式： ',nu)
            return nu
    elif Pr>=0.003 and Pr <= 0.05:
        print('内容待补充2')
        pass

d1=0.012
d2=0.15
v=0.6
tw=80+273.15
t_1=20+273.15
n=4
pi=3.1415926535
l=4*pi*d2
A=pi*pow(d1,2)/4

Cr=1+10.3*pow(2*d1/d2,3)
count=0
for i in range(57,58):
    j=0
    WQE=57.138
    while j <10000000:
        count+=1
        print(count)
        t_2=WQE+273.15
        tf=(t_1+t_2)/2
        re=Re(v,d1,para(p,tf)[2])
        nu=Nu(re,para(p,tf)[4],l,d1,tf,tw,p)
        nu=nu*Cr
        h1=nu*para(p,tf)[3]/d1
        if math.log((tw-t_1)/(tw-t_2))==0:
            h2=h1
        else:
            h2=(para(p,tf)[1]*para(p,tf)[0]*v*A)/(pi*d1*l/math.log((tw-t_1)/(tw-t_2)))
        print(h1-h2,t_2-273.15)
        qwer=h1-h2
        j+=1
        WQE+=0.0000001
        if qwer<=0.0001:
            print(t_2)
            break



