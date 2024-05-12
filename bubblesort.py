array = [1,12,4,6,9,11,8,3,2,15]

def bubblesort(array):
    length = len(array)-1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(0,length):
            if array[i] > array[i+1]:
                sorted = False
                array[i],array[i+1] = array[i+1],array[i]
    return array

print(f"Array: {array}\nSorted Array: {bubblesort(array)}")