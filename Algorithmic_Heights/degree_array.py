#
# Degree Array
#

# Input data
file = open("Data/rosalind_deg.txt","r")
nums = file.readline().split(' ')
n = int(nums[0])
m = int(nums[1])
graph = []

while True:
    l = file.readline().strip('\n').split(' ')
    if l[0] == '':
        break
    else:
        pair = (int(l[0]),int(l[1]))
        graph.append(pair)

# Test values
#n = 6
#m = 7
#graph = [(1,2),(2,3),(6,3),(5,6),(2,5),(2,4),(4,1)]

# Find degrees
for i in range(1,n+1):
    count = 0
    for e in graph:
        if e[0] == i or e[1] == i:
            count += 1
    print(count,end=' ')


