# A program to convert a textual message into a sequence of

def encode():
    print("This program converts a textual message into a sequence \nof numbers, utilizing the underlying Unicode encoding.")

    # Get the message to encode
    message = input("Enter a message: ")
    print("The encoded message is: ", end="")

    # Loop through the message and print out the Unicode values
    list = []
    for ch in message:
        print(ord(ch), end=" ")
        list.append(ord(ch))
    print()
    return list

def decode(list):
    message = ""
    i = int(input("1 for auto 0 for manual:"))
    if i:
        for ch in list:
            codeNum = ch
            message += chr(codeNum)
    else:
        inString = input("Enter a message: ")
        for ch in inString.split():
            codeNum = int(ch)
            message += chr(codeNum)
    print(message)

list = encode()
decode(list)