#File: chaos.py
#A simple program illustrating chaotic behavior.
# def cin(n)
#     for i in range(n):
#
def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a numberA between 0 and 1:"))
    y = eval(input("Enter a numberB between 0 and 1:"))
    n = eval(input("How many numbers should i print?"))
    for i in range(n):
        x =3.9*x*(1-x)
        y =3.9*y*(1-y)
        print(x,y)

main()
