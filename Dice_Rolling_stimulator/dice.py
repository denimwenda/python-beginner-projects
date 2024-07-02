import random
# Categoring outcome into a list

one =   """ 
            ("===========")
            ("|         |")
            ("|    O    |")
            ("|         |")
            ("===========")\n  
        
        """
        
two =   """ 
            ("===========")
            ("|         |")
            ("| O     O |")
            ("|         |")
            ("===========")\n  
        
        """



three =   """ 
            ("===========")
            ("|    O    |")
            ("|    O    |")
            ("|    O    |")
            ("===========")\n  
        
        """

four =   """ 
            ("===========")
            ("|  O    O |")
            ("|     0   |")
            ("|  O    O |")
            ("===========")\n  
        
        """

five =   """ 
            ("===========")
            ("| O     O |")
            ("|    0    |")
            ("| O     O |")
            ("===========")\n  
        
        """

six =  """
            ("===========") 
            ("| O     O |")
            ("| O     O |")
            ("| O     O |")
            ("===========") \n      
        """
        
        
        
outcome_list = [one, two, three, four, five, six]


print("This is a dice stimulator")
x = "y"
while x == "y":
    random_outcome = random.sample(outcome_list, 2)
    for outcome in random_outcome:
        print(outcome)
        
    x = input("Press y to roll again ")