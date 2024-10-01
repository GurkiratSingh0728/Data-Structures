#Question3 : Write a program which finds the location LOC1 of the largest element and the location LOC2 of the second largest element in an array DATA 
#with N > 1 elements. Test the program using 70, 30, 25, 80, 60, 50, 30, 75, 25, and 60.

def findIndexOfTwoLargestNos(arr):
    N = len(arr)   # Number of elements in the array
    
    if N < 1:
        print("Array is empty")
        return
    elif N == 1:
        print("There is only one element in the array")
        return
    
    # Initialize the largest and second largest values and their locations
    largest = second_largest = float('-inf')
    LOCOne = LOCTwo = -1
    
    for index in range(N):
        if arr[index] > largest:
            second_largest = largest  # Update second largest
            LOCTwo = LOCOne            # Update location of second largest
            largest = arr[index]       # Update largest
            LOCOne = index              # Update location of largest
        elif arr[index] > second_largest and arr[index] != largest:
            second_largest = arr[index]  # Update second largest
            LOCTwo = index               # Update location of second largest
    
    if LOCTwo == -1:
        print("There is no second largest element")
    else:
        print(f"LOC1 (largest element): {LOCOne}, LOC2 (second largest element): {LOCTwo}")

# Test the function with the provided array
testingArray = [70, 30, 25, 80, 60, 50, 30, 75, 25, 60]  # Testing array with 10 elements
findIndexOfTwoLargestNos(testingArray)
