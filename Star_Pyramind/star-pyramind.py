cont = "y"
print("Welcome to star pramind generator !")
print()
while cont == "y":
    num = int(input("Enter a number: "))
    
    t = 0
    i = 1
    k = num
    
    while i < (num + 1):
        print(" " * k, end = "")
        j = 0
        
        while j <= t:
            print("*", "", end="")
            j = j + 1
            
        i = i + 1
        t = t + 1
        k = k - 1
        
        print()
        
    cont = input("Do you want to continue? (Enter'y' to continue or 'q' to quit: ").lower()
    