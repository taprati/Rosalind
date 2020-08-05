# Rabbits and Recurrence Relationships


# Inputs
n = 34  # Generations
k = 4  # number of offspring per mating

# Recursive solutions
def rabbits(n,k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return rabbits(n-1,k) + rabbits(n-2,k)*k

print(rabbits(n,k))
    
def rabbit_recursive(n, k):
    if n < 2:
        return n
    else:
        return rabbit_recursive(n-1, k) + rabbit_recursive(n-2, k)*k 

print(rabbit_recursive(n, k))  # Prints 19

# Iterative 
def rabbit_iterative(n, k):
    fn_1, fn_2 = 1, 1
    fn = 1  # Just a place holder in case n is too small
    for _ in range(2, n):
        fn = fn_1 + fn_2*k
        fn_2, fn_1 = fn_1, fn
    return fn
print(rabbit_iterative(n, k))  # Prints 19

