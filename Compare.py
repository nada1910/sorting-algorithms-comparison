import matplotlib.pyplot as plt
from timeit import default_timer as timer
from BubbleSort import bubble_sort
from SelectionSort import selection_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSort import quick_sort
from HeapSort import heap_sort
from GenerateArray import generate_array
input_sizes = [100, 500, 1000, 2000, 3000, 5000]
times_bubble = []
times_selection = []
times_insertion = []
times_merge=[]
times_quick=[]
times_heap=[]
for size in input_sizes:
    arr=generate_array(size)
    #bubble sort
    arr1=arr.copy()
    start_time = timer()
    bubble_sort(arr1)
    end_time = timer()
    times_bubble.append((end_time - start_time) * 1000000)
    #selection sort
    arr2=arr.copy()
    start_time=timer()
    selection_sort(arr2)
    end_time=timer()
    times_selection.append((end_time-start_time)*1000000)
    #insertion sort
    arr3=arr.copy()
    start_time=timer()
    insertion_sort(arr3)
    end_time=timer()
    times_insertion.append((end_time-start_time)*1000000)
    #merge sort
    arr4=arr.copy()
    start_time=timer()
    merge_sort(arr4)
    end_time=timer()
    times_merge.append((end_time-start_time)*1000000)
    #quick sort
    arr5=arr.copy()
    start_time=timer()
    quick_sort(arr5)
    end_time=timer()
    times_quick.append((end_time-start_time)*1000000)
    #heap sort
    arr6=arr.copy()
    start_time=timer()
    heap_sort(arr6)
    end_time=timer()
    times_heap.append((end_time-start_time)*1000000)

plt.figure(figsize=(10, 6))
#Line 1 bubble sort
plt.plot(
    input_sizes, times_bubble, marker='o', color='blue', label='Bubble sort'
)

#Line 2 selection sort
plt.plot(
    input_sizes,
    times_selection,
    marker='o',
    color='red',
    label='Selection sort',
)

#Line 3 insertion sort
plt.plot(
    input_sizes,
    times_insertion,
    marker='o',
    color='orange',
    label='Insertion sort',
)

#Line 4 merge sort
plt.plot(
    input_sizes,
    times_merge,
    marker='o',
    color='purple',
    label='Merge sort',
)

#Line 5 quick sort
plt.plot(
    input_sizes,
    times_quick,
    marker='o',
    color='pink',
    label='Quick sort',
)

#Line 6 heap sort
plt.plot(
    input_sizes,
    times_heap,
    marker='o',
    color='black',
    label='Heap sort',
)


#For assigning color to different algorithms
plt.legend(loc='upper left', frameon=True, shadow=True)
# Formatting axes and labels to match the assignment image
plt.title('Sorting Algorithm Execution Time Comparison')
plt.xlabel('Input size (N)')
plt.ylabel("Execution time (microsec, log scale)")
plt.yscale("log")
plt.grid(True, linestyle='-', alpha=0.5)
plt.tight_layout()
plt.show() #show plot