# 
# Merge Sort
#


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        # Create counters
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
            else:
                arr[k] = right[j]
                k += 1
                j += 1
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
        return arr

# Inputs
#n = 10
#array = [20,19,35,-18,17,-20,20,1,4,4]

#Read file inputs
file = open('Data/rosalind_ms.txt','r')
n = file.readline()
array = [int(i) for i in file.readline().split(' ')]

# Run sort
array = mergeSort(array)
for element in array:
    print(element,end=' ')


