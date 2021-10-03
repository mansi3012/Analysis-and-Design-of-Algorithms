# Python program for implementation of Heap Sort
# n: size of heap
# a: array
# l = left
# r = right

def heapify(a, n, i):
    largest = i # Initializing largest as root
    l = 2*i + 1
    r = 2*i + 2

    # Check if left child of root exists and is greater than the root
    if l < n and a[i] < a[l]:
        largest = l

    # Check if right child of root exists and is greater than the root
    if r < n and a[largest] < a[r]:
        largest = r

    # Change root, if needed
    if largest != i:
        a[i],a[largest] = a[largest],a[i] # swap

        # Heapify the root
        heapify(a, n, largest)


def heapSort(a):
    n = len(a)

    # Build a maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)

    # One by one extract elements
    for i in range(n-1, 0, -1):
        a[i], a[0] = a[0], a[i] # swap
        heapify(a, i, 0)

a = [ 12, 11, 13, 5, 6, 7]
heapSort(a)
n = len(a)
print ("The Sorted array is")
for i in range(n):
    print ("%d" %a[i])
