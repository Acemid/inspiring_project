EPOCH = 15
t1 = 0
t2 = 0
t3 = 0
t4 = 0
a = [t1, t2, t3, t4]
t11=0
t22=0
t33=0
t44=0n 
for i in range(20):
    a = [
     (70 + t2 + t3) / 4,
     (50 + t1 + t4) / 4,
     (25 + t1 + t4) / 4,
     (15 + t2 + t3) / 4
    ]
    if t1 ==0:
        pass
    else:
        t11 = (a[0] - t1)/t1
        t22 = (a[1] - t2)/t2
        t33 = (a[2] - t3)/t3
        t44 = (a[3] - t4)/t4

    t1 = a[0]
    t2 = a[1]
    t3 = a[2]
    t4 = a[3]
    print(i, t1,t11, t2,t22, t3,t33, t4,t44)
