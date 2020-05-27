import cmath, math

def root(a,b,c):
    t = b*b - 4*a*c
    if (t >= 0):
        t2 = math.sqrt(t) #沒有實根
    else :
        t2 = cmath.sqrt(t) #有虛根
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]


print("root of 3x^2+7x+7=", root(3,7,7))
