def quick_sort(arr):
    def sort(low, high):
        if low < high:
            p = partition(arr, low, high)
            sort(low, p)
            sort(p + 1, high)

    sort(0, len(arr) - 1)



#using Hoare partition algorithm
def partition(arr,low,high):

    pivot = arr[(low + high) // 2] #middle element as pivot
    i = low - 1
    j = high + 1

    while (True):

        # Find leftmost element greater than or equal to pivot
        i=i+1
        while (arr[i] < pivot):
            i=i+1

        # Find rightmost element smaller than or equal to pivot
        j -= 1
        while (arr[j] > pivot):
            j=j-1

        # If two pointers met.
        if (i >= j):
            return j

        arr[i], arr[j] = arr[j], arr[i]




