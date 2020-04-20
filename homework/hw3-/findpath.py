import sys
sys.setrecursionlimit(9000000)
def print_map(m):
    for j in range(10):
        for i in range(len(m)):
            if(m[j][i]==1):
                print("口",end="")
            elif(m[j][i]==8):
                print("鼠",end="")
            else:
                print("  ",end="")
            if(i==9):
                print("")
def dfs(m,start,goal,temp,step):
    step+=1
    addr = []
    #tr = []
    temp2 = list(m)
    temp3 = []
    for i in range(10):
        temp3.append(list(temp2[i]))
        #print(temp3)
    temp3[start[0]][start[1]] = 8
    #print(temp3)
    
    if(start[0]+1<10):
        if(m[start[0]][start[1]-1] == 0): 
            addr = (start[0],start[1]-1)
            temp.append(addr)
        #print(temp)
        if(m[start[0]+1][start[1]] == 0): 
            addr = (start[0]+1,start[1])
            temp.append(addr)
        #print(temp)
        if(m[start[0]-1][start[1]] == 0): 
            addr = (start[0]-1,start[1])
            temp.append(addr)
        #print(temp)
        if(m[start[0]][start[1]+1] == 0): 
            addr = (start[0],start[1]+1)
            temp.append(addr)
        print(temp)
        
        start = temp.pop()
        #print(temp)
        temp3[start[0]][start[1]] = 8
        #print(temp)
        #print(start)
        print("step:{:d}".format(step))
        #print(start[1])
        #print(goal[1])
        print_map(temp3)
        print("======================================")
    """
    del m
    m = ()
    tempa = tuple(temp3[0])
    tempb = tuple(temp3[1])
    tempc = tuple(temp3[2])
    tempd = tuple(temp3[3])
    tempe = tuple(temp3[4])
    tempf = tuple(temp3[5])
    tempg = tuple(temp3[6])
    temph = tuple(temp3[7])
    tempi = tuple(temp3[8])
    tempj = tuple(temp3[9])
    m = (tempa,tempb,tempc,tempd,tempe,tempf,tempg,temph,tempi)
    """
    """for i in range(9):
        m = tuple(temp3[i])"""
    #print(m)
    #print_map(temp3)
    #print(temp3[0])
    
    if(start[0] == goal[0] and start[1] == goal[1]):
        return 
    else:
        dfs(temp3,start,goal,temp,step)
        
    
        
m =    ((1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 1, 1, 1, 1, 1, 1, 0, 1, 1),
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
        (1, 0, 1, 1, 0, 1, 1, 1, 1, 1),
        (1, 0, 0, 1, 0, 1, 0, 0, 0, 1),
        (1, 0, 1, 1, 0, 1, 0, 1, 0, 1),
        (1, 0, 1, 1, 1, 1, 0, 1, 0, 1),
        (1, 0, 0, 0, 0, 0, 0, 1, 0, 1),
        (1, 1, 1, 1, 1, 1, 1, 1, 0, 1))
print("================================")
start = [1,0]
#print(start)
goal = [9,8]
temp = []
step = 0
print("Map:")
print_map(m)
print("================================") 
dfs(m,start,goal,temp,step)
print("Task is finished!")
