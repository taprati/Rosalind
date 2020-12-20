# Rosalind Mendel's First Law

# Input
k = 21  # AA
m = 30  # Aa
n = 21  # aa

N = k+m+n

# Calculate Prob(two random mates produce AA)

KK = (k/N)*((k-1)/(N-1))
KN = (k/N)*((n)/(N-1)) 
KM = (k/N)*((m)/(N-1))

MK = (m/N)*((k)/(N-1)) 
MN = (m/N)*((n)/(N-1)) * (1/2)
MM = (m/N)*((m-1)/(N-1)) * (3/4)

NK = (n/N)*((k)/(N-1))
NM = (n/N)*((m)/(N-1)) * (1/2)

probs = [KK,KN,KM,MK,MN,MM,NK,NM]

total_prob = sum(probs)
print(total_prob)


# Alternate
def firstLaw(k,m,n):
   N = float(k+m+n)
   return(1 - 1/N/(N-1)*(n*(n-1) + n*m + m*(m-1)/4.))
