#This is the code to calculate the ASCII conversion.
       



#This takes the input integer of the user.
decimalval = int(input("Enter the decimal value: \n"))


            
#If else functions as a menu


def menu():
    print("[1] Convert to Binary \n ")
    print("[2] Convert to Octal \n")
    print("[3] Convert to Hexadecimal \n")
    print("[0] Exit the program.")
    
menu()
begin = int(input("Select your conversion:"))
    
while begin != 0:
    if begin == 1:
        print("Converted to Binary\n", bin(decimalval))
    elif begin == 2:
        print("Converted to Octal\n", oct(decimalval))
    elif begin == 3:
        print("Converted to Hexadecimal\n", hex(decimalval))
    else:
        print("Invalid option, try again")
    break
        
    
                
    

              

              
              
              