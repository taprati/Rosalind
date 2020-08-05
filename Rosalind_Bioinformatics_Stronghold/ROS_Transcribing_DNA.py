#Problem 2

##An RNA string is a string formed from the alphabet containing 'A', 'C', 'G','U'.
##Given a DNA string t
##corresponding to a coding strand, its transcribed RNA string u
##is formed by replacing all occurrences of 'T' in t
##with 'U' in u
##Given: A DNA string t having length at most 1000 nt.
##Return: The transcribed RNA string of t

file = open('rosalind_rna.txt')
DNA = file.read()
RNA = ''
for char in DNA:
    if char == 'T':
        RNA += 'U'
    else:
        RNA += char
        
#other option: RNA = DNA.replace("T", "U")
print(RNA)
    

