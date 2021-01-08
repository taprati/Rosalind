#
# Counting Inversions
# 


def inversions(arr,n):
    inv = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                inv += 1
    return inv


# Input Data
file = open("Data/rosalind_inv.txt","r")
n = int(file.readline().strip('\n'))
array = [int(i) for i in file.readline().strip('\n').split(' ')]

# Run inversions
inversion_count = inversions(array,n)
print(inversion_count)

