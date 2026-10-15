
def heapfy(arr, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapfy(arr, largest, n)


def build_maxheap(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapfy(arr, i, n)


def heap_sort(arr):
    build_maxheap(arr)
    n = len(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapfy(arr, 0, i)

    return arr


def main():
    arr = [4, 10, 3, 5, 1]
    heap_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()

