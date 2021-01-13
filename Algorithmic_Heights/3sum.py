#
# 3SUM
#


def threeSum(arr, total):
    length = len(arr)
    
    # Start with one number
    for first in range(length-1):
        
        s = set()
        # Find second number
        for second in range(first+1,length):
            third = total - (arr[first] + arr[second])
            # Check for existence of third number
            if third in s:
                ind = arr.index(third,first)
                if second < ind:
                    print(first+1, second+1, ind+1)
                    return None
                else:
                    print(first+1, ind+1, second+1)
            else:
                s.add(arr[second])
    print(-1)
    return None 


#Read file inputs
file = open('Data/rosalind_3sum.txt','r')
k, n = file.readline().strip('\n').split(' ')

# Run 3SUM
total = 0
for line in file:
    array = [int(i) for i in line.split(' ')]
    threeSum(array, total)

