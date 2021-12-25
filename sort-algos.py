def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot-1)
        quick_sort(arr, pivot+1, right)
    
def partition(arr, low, high):
    left, pivot_ind = low, low
    right = high
    pivot = arr[pivot_ind]
    while left < right:
        while arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1    
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[pivot_ind], arr[right] = arr[right], arr[pivot_ind]    
    return pivot_ind

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                k += 1
            else:
                arr[k] = R[j]
                j += 1
                k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1   

arr = [3,1,28,54,33,12,9]
#quick_sort(arr, 0, len(arr)-1)
#merge_sort(arr)
#print(f'Sorted array: {arr}')