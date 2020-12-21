# 
# Enumerating Gene orders
#

from itertools import permutations 

n = 5

nums = []
for i in range(1,n+1):
    nums.append(i)

perms = permutations(nums)

print(len(list(perms)))

perms = permutations(nums)

for i in list(perms):
    for j in i:
        print(j,end=' ')
    print('',sep='\n')


