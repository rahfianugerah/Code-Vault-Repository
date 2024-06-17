def insertionsort(arr):
  # Traverse through 1 to len(arr)
  for i in range(1, len(arr)):
    key = arr[i]
    # Move elements of arr[0..i-1]
    j = i-1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  # Print the sorted array
  print("Sorted Array:", arr)
# Driver code
arr = [12, 11, 13, 5, 6]
insertionsort(arr)
