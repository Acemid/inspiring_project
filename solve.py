import numpy as np
import os

if __name__=='__main__':
    a=int(input('A为几维矩阵：'))
    A=[]
    for i in range(a):
        A.append([])
        for c in range(a):
            A[i].append(int(input("行的数值:")))


    A=tuple(A)


    B=[]

    b=int(input('B的列数：'))
    for i in range(b):
        d=int(input(('B的列值:')))
        B.append(d)


    B=tuple(B)
    x = np.linalg.solve(A,B)
    print(x)
    os.system('pause')


#pyinstaller --onefile 文件名.py