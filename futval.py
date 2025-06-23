# A program to compute the value of an investment
# carried 10 years into the future
from tkinter.font import names
import math
from graphics import * #import functions from graphics.py
#main caculates property
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")
    principal = float(input("Enter the property value: "))
    property = principal
    apr = float(input("Enter the annual rate: "))
    for i in range(10):
        property = property*(1+apr)
    return (principal,property,apr)
# windows generate a chart
def windows(principal,property,apr):
    win = GraphWin("Investment Growth Chart", 640, 480)
    origin = Point(30,460)
    hmax = math.ceil(property/100) /10
    hlow = math.floor(principal/100) /10
    temp = principal/1000
    names = locals()
    if principal <= 999999:
        Text(origin,"(K)/Year").draw(win)
    elif principal > 999999:
        Text(origin, "(M)/Year").draw(win)
        hmax = hmax/1000
        hlow = hlow/1000
        temp = temp/1000
    floor = (hmax - hlow) / 10
    Text(Point(320, 20), 'press <Enter> key to exit').draw(win)
    Line(Point(80, 460), Point(620, 460)).draw(win)
    line = Line(Point(80,460), Point(80,40))
    line.setArrow('last')
    line.draw(win)
    for i in range(11):
        names['h' + str(i) ] = Point(30,460-40*i)
        if i >= 1:
            temp = temp*(1+apr)
            num = round(hlow + floor * i,2)
            Text(names['h' + str(i)], num).draw(win)
            bar = Rectangle(Point(50+50*i,(60*(hlow-hmax)+400*(temp-hmax))/(hlow-hmax)),Point(100+50*i,460))
            bar.setFill('green')
            bar.setWidth(2)
            bar.draw(win)
            Text(Point(75+50*i,-20+(60*(hlow-hmax)+400*(temp-hmax))/(hlow-hmax)),round(temp,1)).draw(win)

principal,property,apr = main()
print("The final property:","{:,}".format(round(property,2)))
windows(principal,property,apr)
input("press <Enter> key to exit")
