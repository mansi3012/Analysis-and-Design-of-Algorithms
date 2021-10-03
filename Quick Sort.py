# Python program for implementation of QuickSort
# Pointer start: points to first element of array
# Pointer end: points to last element of array
# Array a

def partition(start, end, a):
    pivot_index = start
    pivot = a[pivot_index]

    while start < end:

        # Increment the start pointer till an element greater than pivot is found
        while start < len(a) and a[start] <= pivot:
            start += 1

        # Decrement the end pointer till an element less than pivot is found
        while a[end] > pivot:
            end -= 1

        # If start and end have not crossed each other then swap the numbers on start and end
        if (start < end):
            a[start], a[end] = a[end], a[start]

    # Swaping the pivot element with element on end pointer.
    a[end], a[pivot_index] = a[pivot_index], a[end]

    # Return end pointer to divide the array into 2
    return end

def QuickSort(start, end, a):
    if (start < end):
        p = partition(start, end, a)

        QuickSort(start, p - 1, a)
        QuickSort(p + 1, end, a)

a = [45,73,12,52,71,36,85]
QuickSort(0, len(a) - 1, a)

print('The Sorted Array is:',a)