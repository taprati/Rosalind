#
# Merge Two Sorted Arrays
#
# Given: A positive integer n <= 10^5 and an array A[1..n] of integers, and m <= 10^5 and array B[1..m]
# Return: A sorted array C[1..n+m]
#


def merge_sorted_arrays(array_A, array_B, l1, l2):
    merged = [None for x in range(l1+l2)]
    i = 0
    j = 0
    k = 0
    while i < l1 and j < l2:
        if array_A[i] < array_B[j]:
            merged[k] = array_A[i]
            i += 1
            k += 1
        else:
            merged[k] = array_B[j]
            j += 1
            k += 1
    while i < l1:
        merged[k] = array_A[i]
        i += 1
        k += 1
    while j < l2:
        merged[k] = array_B[j]
        j += 1
        k += 1

    return merged


# Open file and get data
file = open("Data/rosalind_mer.txt", 'r')
n = int(file.readline())
A = [int(i) for i in file.readline().split(' ')]
m = int(file.readline())
B = [int(i) for i in file.readline().split(' ')]
file.close()

# Run Merge
C = merge_sorted_arrays(A, B, n, m)
for i in range(len(C)):
    print(C[i], end=" ")
