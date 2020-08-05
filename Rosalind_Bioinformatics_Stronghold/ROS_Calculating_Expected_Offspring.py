# Calculating Expected Offspring

# Open file
file = open("rosalind_iev.txt", 'r').read()
nums = file.split()

# Test case
# nums = [1, 0, 0, 1, 0, 1]

offspring = 2

AA_AA = float(nums[0])
AA_Aa = float(nums[1])
AA_aa = float(nums[2])
Aa_Aa = float(nums[3])
Aa_aa = float(nums[4])
aa_aa = float(nums[5])

total_offspring = 0

total_offspring += AA_AA * offspring * 1
total_offspring += AA_Aa * offspring * 1
total_offspring += AA_aa * offspring * 1
total_offspring += Aa_Aa * offspring * 0.75
total_offspring += Aa_aa * offspring * 0.5
total_offspring += aa_aa * offspring * 0

print(total_offspring)
