def selection_sort(array):
    length=len(array)
    for i in range (length-1):
        minIndex=i
        for j in range(i+1,length):
            if array[j]<array[minIndex]:
                minIndex = j
        array[i],array[minIndex]=array[minIndex],array[i]
    return array
array=[21,3,6,33,9]
print("The sorted array is:",selection_sort(array))