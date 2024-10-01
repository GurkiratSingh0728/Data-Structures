#Question2: Write a program using DIV(J, K) which reads a positive integer N > 10 and determines whether or not N is a prime number. (Hint: N is prime if DIV(2, N) = 0 (i.e., N is odd)
#and DIV(K, N) = 0 for all odd integers K where 1 < K^2 ≤ N.)

print("Please enter the two number K") #Taking user input
j = 2  
k = input("K = ")

try:
    j = int(j)  #Converting the input to integer
    n = int(k)  #Converting the input to integer
except ValueError:
    print( "Invalid input. Please enter a positive integer.")  #If the input is not a positive integer, print an error message and exit the program

def division(j, n): #Function to check if j divides k
    if n <= 10:
        print("Please enter a number greater than 10") #If the number is less than or  equal to 10, print an error message and exit the program
    
    if n%j == 0:  #Checking if k is divisible by j
        print(f'Number {n} is even') #If n is divisible by j, print the result as even
    elif n%j == 1: 
        print(f'Number {n} is odd') #If n is divisible by j, print the result as odd
    elif j != int(j) and k != int(k): #user enters a value that isn't an integer
        print("Please enter valid values")

division(j, k)  #Calling the function with the user input values3