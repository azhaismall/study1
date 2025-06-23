# A program to change km to mile

def main():
    type = int(input("enter <1> to change km to mile\nenter <2> to change mile to km\n"))
    distance = eval(input("Enter the ndistance:"))
    if type == 1:
        distance = 0.62*distance
        print("The distance in mile is",distance)
    if type == 2:
        distance = distance/0.62
        print("The distance in km is",distance)

main()
input("Press Enter to Exit")