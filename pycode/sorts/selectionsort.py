# Selection Sort
array = [64, 25, 12, 22, 11]
print(f"Unsorted Array: {array}")
# Traverse through all array elements
for i in range(len(array)-1):
    # Find the minimum element in remaining 
    # Unsorted array
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j            
    # Swap the found minimum element with 
    # The first element        
    array[i], array[min_idx] = array[min_idx], array[i]
# Driver code to test above
print (f"Sorted Array: {array}")
