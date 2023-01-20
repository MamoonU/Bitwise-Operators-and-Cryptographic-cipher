#Task 1 - Bitwise Operations

a = int(input("Is your first variable a 1 or 0? ")) #asks for first variable from the user
b = int(input("Is your second variable a 1 or 0? ")) #asks for seecond variable from the user
    

def AND(a, b): #function which uses the AND bitwise operator
    return a & b

def OR(a, b): #function which uses the OR bitwise operator
    return a | b
    
def XOR(a, b): #function which uses the XOR bitwise operator
    return a ^ b


print("AND = ") #Prints AND, OR and XOR for the user based on which variables the user inputted
print(AND(a, b)) 
print("OR = ")
print(OR(a, b))
print("XOR = ")
print(XOR(a, b))



#Task 2 - Cryptographic cipher using ASCII conversion

#here i name my important variables

ordx = 0 # ordx = ascii number of the characters
new_ordx = 0 # new_ordx = shifted ascii number of the characters (ascii number + key)
encrypted_pass = [] # making a variable i can use as a list later to concatenate

def encryption(password, key): #encryption function (arguments to pass variables across functions)
    for character in password: #for each character in password
        ordx = ord(character) #convert each character to ascii number
        new_ordx = ordx + key #add ascii number and key to make new_ordx
        if new_ordx < 33 or new_ordx > 126: #if the ascii number is greater than or less than useable numbers/letters/symbols, then it will make the character null
            continue 

        new_pass = chr(new_ordx) #converting the ascii numbers back into characters
        encrypted_pass.append(new_pass) 

    final_pass = ''.join(encrypted_pass) #adding each character back together by appending them to an empty list

    print(final_pass) #prints final encrypted password
    
def main(): #main function
    password = input("Enter your password (Please only include numbers or letters): ") #asks the user for a password including only letters or numbers
    key = int(input("Select a key between 1 and 15: ")) #asks for a key (number between 1-15)

    if key <= 0 or key >= 16: #if key is smaller or equal to 0 then it will call back to the beginning of the function
        main() #this is to call the main function again

    encryption(password, key) #encryption function (arguments to pass variables across functions)

if __name__ == '__main__': #calls the main function first
    main()










#notes




#im converting the new ordx to string from bytes

#ive printed each character back to string. i need it together

#new pass is now global. new pass is the shifted password which has been returned to char

#i want the encrypted pass to be all the shifted password characters together

#i need to make the new pass into a list, then concatenate the items of that list

#need to save the new pass into the list (encrypted_pass)

#need to convert items in the list into a string

#if new_ordx greater than it should be, then it wraps around to the lowest number available