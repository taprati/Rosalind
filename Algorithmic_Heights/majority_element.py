# 
# Majority Element
# 

def majorityElement(arr,n):
    counted = []
    for i in arr:
        if i not in counted:
            counted.append(i)
            c = arr.count(i)
            if c > (n//2):
                return i
    return -1


# Read in file
file = open("Data/rosalind_maj.txt","r")
kn = file.readline().strip('\n').split(' ')
k = int(kn[0])
n = int(kn[1])
lists = []

for l in file:
    array = [int(i) for i in l.strip('\n').split(' ')]
    lists.append(array)

# Find Majority Element
majority_elements = []
for a in lists:
    majority_elements.append(majorityElement(a,n))

for i in majority_elements:
    print(i,end=' ')

