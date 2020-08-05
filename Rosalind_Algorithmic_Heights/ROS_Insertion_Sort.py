#
# Insertion Sort
#
# Given: A positive integer n <= 10^3 and an array A[1..n] of integers
# Return: The number of swaps performed by insertion sort algorithm
#


def insertion_sort(nums):
    swaps = 0
    for i in range(len(nums)):
        k = i
        while k > 0 and nums[k] < nums[k-1]:
            nums[k-1], nums[k] = nums[k], nums[k-1]
            k = k-1
            swaps += 1
    return nums, swaps


# Open file and get data
file = open("Data/test.txt", 'r')
n = int(file.readline())
A = [int(i) for i in file.readline().split(' ')]
file.close()

# Run sort
A_sorted, swap_count = insertion_sort(A)
print(A_sorted)
print("Number of Swaps:", swap_count)
