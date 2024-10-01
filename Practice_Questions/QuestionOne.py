#Question1: Write a functiion, DIV(J, K), where J and K are positive integers such that DIV(J, K) = 1 when J divides K
# but otherwise DIV(J, K) = 0 when J doesn't divide K

print("Please enter the two numbers J and K respectively") #Taking user input
j = input("J = ")  #Taking user inputs
k = input("K = ")  

try:
    j = int(j)  #Converting the input to integer
    k = int(k)  #Converting the input to integer
except ValueError:
    print( "Invalid input. Please enter a positive integer.")  #If the input is not a positive integer, print an error message and exit the program

def division(j, k): #Function to check if j divides k
    if k%j == 0:  #Checking if k is divisible by j
        print("1 \nFinal Statement: " + str(k) + " is divisible by " + str(j)) 
    elif k%j != 0: 
        print("0 \nFinal Statement: " + str(k) + " is not divisible by " + str(j))
    elif j != int(j) and k != int(k): #user enters a value that isn't an integer
        print("Please enter valid values")

division(j, k)  #Calling the function with the user input values3