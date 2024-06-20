def addressVal(address):
    dot = address.find(".")
    at = address.find("@")
    if (dot == -1):
        print("Invalid")
    elif (at == -1):
        print("Invalid")
    else:
        ("Valid")


print("This program will decideif your input is a valid email addresss.")
while True:
    print("A valid email address needs an '@' sysmbol and a '.'")
    x = input("Input our email address: ")

    addressVal(x)