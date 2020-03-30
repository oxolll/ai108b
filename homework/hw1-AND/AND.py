import numpy as np
import gd as gd
#from numpy.linalg import norm

A = np.array([[0.0,0,1],
                [1,0,1],
                [0,1,1],
                [1,1,1]])

B = np.array([0.0,0,0,1]).transpose()

def f(p):
    X = p
    Y = A.dot(X)
    return np.linalg.norm(Y-B,2)

def sig(x):
    s = 1.0 / (1.0+ np.exp(-x))
    return s

p = np.array([0.0,0.0,0.0])
p = gd.gradientDescendent(f,p,step=0.01)

print("                              ")

print("p={}".format(p))

xy = np.array([p[0],p[1]])
b = p[2]

inputArr = np.array([[0.0,0],
                    [0,1],
                    [1,0],
                    [1,1]])

inputArr1 = np.array([[0.0,0],
                    [0,1],
                    [1,0],
                    [1,1]])                    

ans = np.array([0.0,0.0,0.0,0.0])
###print("{}".format(inputArr[2][1]))

#print("{}".format(inputArr[1][1]*xy[1]))
for i in range(1,5):
    #print("{}".format(i))
    for j in range(1,2):
        inputArr[i-1][j-1] = inputArr[i-1][j-1] * xy[j-1]
        #print("{}",inputArr[i-1][j-1])

for i in range(1,5):
        ans[i-1] = sig(inputArr[i-1][0] + inputArr[i-1][1] + b)

    #B = np.dot(inputArr[i],xy) + b
print("inputs: \n{}".format(ans))
#print("f(x,y,b)= ||(A·X)-B|| :\n{}".format(B))
print("sig(f(x,y,b)) = \n{}".format(ans))

#ans = []
for i in range(1,5):
    if sig(ans[i-1]) <= 0.5:
        ans[i-1] = 0
    else:
        ans[i-1] = 1


print("Output = {}".format(ans))
print("\n\n")

print("xy: {}".format(xy))
print("b: {}".format(b))

print("\n\n")

print("\tInputs  |  Outputs")
for i in range(len(ans)):
    print("\t{}\t\t{}".format(inputArr1[i], ans[i]))