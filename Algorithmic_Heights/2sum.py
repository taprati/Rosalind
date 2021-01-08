#
# 2SUM
#


def twoSum(arr, total):
    # Sort array
    length = len(arr)
    #arr = sorted(arr)
    # search for complement
    for i in range(length):
        complement = int(total - arr[i])
        try:
            search = arr.index(complement,i+1)
        except ValueError:
            search = -1
        if search != -1:
            print(i+1,search+1)
            return None
    print(-1)
    return None


#Read file inputs
file = open('Data/rosalind_2sum.txt','r')
k, n = file.readline().strip('\n').split(' ')

# Run 2SUM
total = 0
for line in file:
    array = [int(i) for i in line.split(' ')]
    twoSum(array, total)

