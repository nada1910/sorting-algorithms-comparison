from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from HeapSort import heap_sort
from GenerateArray import generate_array
from timeit import default_timer as timer

def main():
    arr = generate_array(10)
    print("Original array:", arr)

    # Selection sort
    arr1 = arr.copy()#copy 
    start = timer()
    selection_sort(arr1)
    end = timer()
    selection_time = (end - start) * 1000

    # Bubble sort
    arr2 = arr.copy()
    start = timer()
    bubble_sort(arr2)
    end = timer()
    bubble_time = (end - start) * 1000

    # Insertion sort
    arr3 = arr.copy()
    start = timer()
    insertion_sort(arr3)
    end = timer()
    insertion_time = (end - start) * 1000

    # Merge sort
    arr4 = arr.copy()
    start = timer()
    merge_sort(arr4)
    end = timer()
    merge_time = (end - start) * 1000

    #Quick sort
    arr5 = arr.copy()
    start = timer()
    quick_sort(arr5)
    end = timer()
    quick_time = (end - start) * 1000 

    #Heap sort
    arr6 = arr.copy()
    start = timer()
    heap_sort(arr6)
    end = timer()
    heap_time = (end - start) * 1000  

    print("\nFinal sorted array:", arr1)
    print("Running times:")
    print(f"Bubble sort: {bubble_time:.6f} ms") 
    print(f"Selection sort: {selection_time:.6f} ms") 
    print(f"Insertion sort: {insertion_time:.6f} ms")
    print(f"Merge sort: {merge_time:.6f} ms")
    print(f"Quick sort: {quick_time:.6f} ms")
    print(f"Heap sort: {heap_time:.6f} ms")
if __name__ == "__main__":
    main()