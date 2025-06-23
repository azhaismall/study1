import math
def ball():
    r = float(input("Enter a radius: "))
    V = 4/3*math.pi*r**3
    S = 4*math.pi*r**2
    print("The volume is:",V,"\nThe surface area is:",S)

def pizza_cost():
    d = float(input("Enter a diameter: "))
    c = float(input("Enter cost per square inch: "))
    s = (0.5*d)**2*math.pi
    cost = round(s*c,2)
    print("The cost is:",cost)

def distance():
    diff = float(input("Enter a time difference: (s)"))
    d = round(diff*(299792458*340)/(299792458-340)/1000,3)
    print("The distance is:",d,"(km)")

def slope():
    x1,y1 = eval(input("Enter x1 and y1 values: "))
    x2,y2 = eval(input("Enter x2 and y2 values: "))
    slope = (y2-y1)/(x2-x1)
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The slope is:",slope)
    print("The distance is:",distance)

def sqrt():
    x = eval(input("Enter x: "))
    guess = x/2
    while abs(guess**2-x)>0.00000001:
        guess = (guess+x/guess)/2
    print("The root is:",round(guess,8))





