# 
# Binary Search
#
# 

def binary_search(l,k,start,end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if k == l[mid]:
        return mid + 1
    elif k > l[mid]:
        return binary_search(A,k,mid+1,end)
    elif k < l[mid]:
        return binary_search(A,k,start,mid-1)


# Open file and get data
file = open("Data/rosalind_bins.txt", 'r')
n = int(file.readline())
m = int(file.readline())
A = [int(i) for i in file.readline().split(' ')]
L = [int(i) for i in file.readline().split(' ')]
file.close()

# test
# n = 5
# m = 6
# A = [10, 20, 30, 40, 50]
# L = [40, 10, 35, 15, 40, 20]

# Run binary search
list_of_indexes = []
for i in L:
    list_of_indexes.append(binary_search(A,i,0,n))

for num in list_of_indexes:
    print(num,end=' ')

