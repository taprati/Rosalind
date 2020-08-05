import math


def nck(n, k):  # N choose K
    f = math.factorial
    return f(n) / f(k) / f(n - k)


N = 18  # Number of Individuals
K = 6  # Number of gens
pop = 2 ** K  # pop at k gens

# Calculate Probability
probability = 0
for i in range(N, pop + 1):
    prob = (nck(pop, i)) * (0.25 ** i) * (0.75 ** (pop - i))
    probability += prob

print(probability)
