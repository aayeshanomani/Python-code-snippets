import numpy as np
import pandas as pd

my_list = [1,2,3]
x = np.array(my_list)
y = np.array([4,5,6])
print('x',x)
n = np.arange(0,30,2)
print('n',n)
m = np.array((x,y))
print('m',m)
n = n.reshape(3,5)
print('n reshape',n)
o = np.linspace(0,4,9)
print('o linspace',o)
o = o.resize(3,3)
print('o resize',o)
print(np.ones((3,2)))
print(np.zeros((4,3)))
print(np.eye(6))
print(np.diag(x))
print(np.array(x*3))
print(np.array([1,2,3]*3))
print(np.repeat([1,2,3],3))
print(np.ones([2,3],int))
p = np.ones([2,3],int)
print(np.vstack([p, 2*p]))
print(np.hstack([p,2*p]))
print(x+y,x*y,x**2)
print(x.dot(y))
z = np.array([y,y**2])
print(z)
print(z.shape)
print(z.T)
print(z.T.shape)
print(np.arange(36))
x = np.arange(36)
x = x.reshape(6,6)
print(x)
print(x[0:4,0:6])
print(x[0:6, ::7])
print(x[0:6, ::-7])
print(x[:,::7])
print(x.reshape(36)[::7])
print(z.dtype)
print(z.astype('f'))
a = np.array([-4,-2,1,3,5])
print(a.sum())
print(a.max())
print(a.min())
print(a.mean())
print(a.std())
print(a.argmax())
print(a.argmin())
s = np.arange(13)**2
print(s)
print(s[0],s[4],s[0:4],s[-4:])
print(s[-5::-2])

#iterating over

test = np.random.randint(0,10,(4,3))
print(test)
for row in test:
    print(row)
for i in range(len(test)):
    print(test[i])
for i, row in enumerate(test):
    print('row',i,'is',row)
test2 = test ** 2
print(test2)
for i,j in zip(test,test2):
    print(i,'+',j,'=',i+j)