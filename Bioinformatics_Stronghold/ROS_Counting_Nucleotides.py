# Problem 1 on rosalind
# Given a DNA string s of length at most 1000 nt
# Return four integers (separated by spaces) counting
# the respective number of times
# that the symbols 'A', 'C', 'G', and 'T' occur in s


file = open('rosalind_dna.txt')
s = file.read()
A_count = 0
C_count = 0
G_count = 0
T_count = 0

for char in s:
    if char == 'A':
        A_count += 1
    if char == 'C':
        C_count += 1
    if char == 'G':
        G_count += 1
    if char == 'T':
        T_count += 1

print(A_count,' ',C_count,' ',G_count,' ',T_count)
