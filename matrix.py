# numpy模組 - 基本用法:創建矩陣
import numpy as np

#建立一個 np array
#放入list就會轉換
#印出 3*3 矩陣

#i.
array_A = np.array([
                [1,2,3],
                [4,5,6],
                [7,8,9]
])    
print ('Matrix A (3,3):','\n',array_A)


array_B = np.array([
                [9,8,7],
                [6,5,4],
                [3,2,1]
])
print ('Matrix B (3,3):','\n',array_B)

print('='*10,'A+B','='*10)

#ii.
print (array_A + array_B)

print('='*10,'A-B','='*10)

#iii.
print (array_A - array_B)

print('='*10,'A*B','='*10)

#iv.
print (array_A * array_B)

print('='*5,'the travspose of A*B','='*5)

#v.
print((array_A * array_B).T)