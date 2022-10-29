'''
    PRINT SUBSET SUM

    Given an array of integers and a sum, the task is to print all
    subsets of the given array with a sum equal to a given sum.
'''


def print_subset_sum(arr, target, i=0, a=[]):
    if target == 0:
        return [a]
    if i == len(arr):
        return []
    count = []
    if arr[i] <= target:
        count += print_subset_sum(arr, target - arr[i], i + 1, a + [arr[i]]) + print_subset_sum(arr, target, i + 1, a)
    else:
        count += print_subset_sum(arr, target, i + 1, a)
    return count 

array = [2, 3, 5, 6, 8, 10]
req_sum = 10
for i in print_subset_sum(array, req_sum):
    print(*i)