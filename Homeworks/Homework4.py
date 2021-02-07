numbers=list(range(2,100))
def check(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True
for i in range(100):
    if(check(i)==True):
        print(i," is a prim number\n")