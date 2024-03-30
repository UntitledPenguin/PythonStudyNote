
# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot
 
import random
 
#Partition position:
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high): # Move the numbers lower than the pivot to the left
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    #After moving all the i numbers to the left side of the pivot, put the pivot in the right place: that is the i+1 in the list
    (array[i + 1], array[high]) = (array[high], array[i + 1])
     # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort

def quickSort(array, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        # making sure there is at least two items in the list to sort
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)
 
n=int(input())
arr=[]
scale=int(input())
for k in range(n):
    arr.append(random.randint(0, scale))

print("Unsorted Array")
print(arr)

l = len(arr)
 
quickSort(arr, 0, l-1)
print('Sorted Array(Ascending Order):')
print(arr)