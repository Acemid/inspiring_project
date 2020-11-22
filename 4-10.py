import matplotlib.pyplot as plt
from matplotlib import animation

EPOCH = 15
t1 = 373.15
t2 = 273.15
t3 = 273.15
t4 =273.15
H=0.045
a=50.0
b=0.01
tf=293.15
h=50.0

t22=0
t33=0
t44=0

c = [t2, t3, t4]

plt.ion()
x1=[0,0]
y1=[0,0]
y2=[0,0]
y3=[0,0]

for i in range(50):
    c = [
    (2 * H * h * tf / 3 + 3 * a * b * (t1 + t3)/ H )/(2 * H * h / 3+6 * a * b / H  ),
    (2 * H * h * tf / 3 + 3 * a * b * (t2 + t4)/ H )/(2 * H * h / 3+6 * a * b / H  ),
    (2 * H * h * tf / 3 + 3 * a * b *t3 / H) / (2 * H * h / 3 + 3 * a * b / H)
    ]
    d=i
    if t3 ==0:
        pass
    else:
        t22 = (c[0] - t2)/t2
        t33 = (c[1] - t3)/t3
        t44 = (c[2] - t4)/t4
    if t22 <=0.0002 and t33 <=0.0002 and t44 <=0.0002 :
        print()
    x1[0]=x1[1]
    y1[0]=y1[1]
    x1[1]=i
    y1[1]=t22
    y2[0]=y2[1]
    y2[1]=t33
    y3[0] = y3[1]
    y3[1] = t44
    plt.title('绝热')

    plt.plot(x1,y1,color='red',label='t22')
    plt.plot(x1,y2,color='green',label='t33')
    plt.plot(x1,y3,color='blue',label='t44')
    if i == 0:
        plt.legend(loc='upper right', fontsize=10)
    plt.pause(0.05)

    t2 = c[0]
    t3 = c[1]
    t4 = c[2]

    print(i,'绝热', t2,t22,t3,t33,t4,t44)

plt.ioff()
plt.show()
print()
plt.cla()
EPOCH = 15
t1 = 373.15
t2 = 273.15
t3 = 273.15
t4 = 273.15
H=0.045
a=50
b=0.01
tf=293.15
h=50

t22=0
t33=0
t44=0


c = [t2, t3, t4]

plt.ion()
x1=[0,0]
y1=[0,0]


for i in range(50):
    c = [
    (2 * H * h * tf / 3 + 3 * a * b * (t1 + t3)/ H )/(2 * H * h / 3+6 * a * b / H  ),
    (2 * H * h * tf / 3 + 3 * a * b * (t2 + t4)/ H )/(2 * H * h / 3+6 * a * b / H  ),
    (H * h * tf + 3 * a * b * t3 / H) / ( H * h + 3 * a * b / H)
    ]
    if t3 ==0:
        pass
    else:
        t22 = (c[0] - t2)/t2
        t33 = (c[1] - t3)/t3
        t44 = (c[2] - t4)/t4
    if t22 <=0.0002 and t33 <=0.0002 and t44 <=0.0002 :
        print()
    x1[0]=x1[1]
    y1[0]=y1[1]
    x1[1]=i
    y1[1]=t22
    y2[0]=y2[1]
    y2[1]=t33
    y3[0] = y3[1]
    y3[1] = t44
    plt.title('对流')
    plt.plot(x1,y1,color='red',label='t22')
    plt.plot(x1,y2,color='green',label='t33')
    plt.plot(x1,y3,color='blue',label='t44')
    if i == 0:
        plt.legend(loc='upper right', fontsize=10)
    plt.pause(0.05)

    t2 = c[0]
    t3 = c[1]
    t4 = c[2]

    print(i,'对流', t2,t22,t3,t33,t4,t44)

plt.ioff()
plt.show()
print()

