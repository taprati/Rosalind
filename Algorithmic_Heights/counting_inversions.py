# 
# Counting Inversions
#

def countingInversions(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        left, li = countingInversions(left)
        right, ri = countingInversions(right)
        sorted_arr = []

        i = 0
        j = 0
        inv = 0 + li + ri

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1
                # Right < left, so everything element still in left is inversion
                inv += (len(left)-i)
        sorted_arr += left[i:]
        sorted_arr += right[j:]
    return sorted_arr, inv


#Read file inputs
file = open('Data/rosalind_inv.txt','r')
n = file.readline()
array = [int(i) for i in file.readline().split(' ')]

# Call inversion count
sarray, inversions = countingInversions(array)
print(inversions)
