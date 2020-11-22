from CoolProp.CoolProp import PropsSI
import math
#横掠圆管

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
    D=PropsSI('D', 'P', p, 'T', t, 'air')
    C = PropsSI('C', 'P', p, 'T', t, 'air')
    V = PropsSI('V', 'P', p, 'T', t, 'air')
    λ = PropsSI('L', 'P', p, 'T', t, 'air')
    Pr=PropsSI('Prandtl', 'P', p, 'T', t, 'air')
    return [D,C,V,λ,Pr]

#U=D`V
#a=V/Pr

def Re(v,d,V):
    re=v*d/V
    return  re

def Nu(Re,Pr):
    if Re>=0.4 and Re<4 :
        C=0.989
        n=0.33
        Nu = C * pow(Re, n) * pow(Pr, 1 / 3)
        print('C,n确定的',Nu)
    elif Re>=4 and Re<40:
        C = 0.911
        n = 0.385
        Nu = C * pow(Re, n) * pow(Pr, 1 / 3)
        print('C,n确定的',Nu)
    elif Re>=40 and Re<4000:
        C = 0.683
        n = 0.466
        Nu = C * pow(Re, n) * pow(Pr, 1 / 3)
        print('C,n确定的',Nu)
    elif Re>=4000 and Re<40000:
        C = 0.193
        n = 0.618
        Nu = C * pow(Re, n) * pow(Pr, 1 / 3)
        print('C,n确定的',Nu)
    elif Re>=40000 and Re<400000:
        C = 0.0266
        n = 0.805
        Nu = C * pow(Re, n) * pow(Pr, 1 / 3)
        print('C,n确定的',Nu)
    else:
        Nu=0.3+0.62*pow(Re,1/2)*pow(Pr,1/3)*pow(1+pow(Re/282000,5/8),4/5)/pow(1+pow(0.4/Pr,2/3),1/4)
        print('丘吉尔公式：',Nu)
    return Nu

λ=35
H=0.1
d_wai=0.01
d_nei=0.006
t_1=180
t_2=100
u=5

t=180+273.15
for i in range(0,200,1):
    t=t+i*0.1
    re=Re(u,d_wai,para(p,t)[2])
    nu=Nu(re,para(p,t)[4])
    h=nu*para(p,t)[3]/d_wai
    m=pow(4*h/(d_wai*λ),1/2)
    a=math.cosh(m*H)
    t_f=((a*t_1)-(t_2))/(a-1)+273.15
    print('t',t-273.15,'tf',t_f-273.15,'bias',t-t_f)
    bias=t-t_f
    t=180+273.15
    if bias>0:
        break

