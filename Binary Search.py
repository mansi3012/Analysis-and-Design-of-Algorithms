# Binary Search using Python
# Array a
# Left l, Right r

def BinarySearch(a, l, r, item):
    if r >= l:
        mid = (r + l) // 2

        if a[mid] == item:
            return mid
        elif a[mid] > item:
            return BinarySearch(a, l, mid - 1, item)
        else:
            return BinarySearch(a, mid + 1, r, item)
    else:
        return -1

a = [10,20,30,40,50,60]
item = 30

result = BinarySearch(a, 0, len(a)-1, item)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in the array")

