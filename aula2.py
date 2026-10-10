import math

def bhaskara(a, b, c):
    delta =( b * b - 4 * a * c)
    print(delta)
    
    if delta > 0:
        x1 = -b + math.sqrt(delta) / (2 * a)
        x2 = -b + math.sqrt(delta) / (2 * a)
        print(x1, x2)


def cidadeEpais(c, p):
    print ( c + " esta localizado em"+ p)



cidadeEpais("Vitoria", "brasil")



def calculeomaior(x, y, z):
    if x>y and x>z:
        print("maior", x)
    elif y>x and y>z:
        print("maior", y)
    else:
        print("maior", z)
        
        
calculeomaior(10, 25, 3)
        
        
        

