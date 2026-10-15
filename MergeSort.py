def merge(left,right,arr):
    left_size = len(left)
    right_size = len(right)
    i=r=l=0 #r for right array ad l for left array
    while(r<right_size and l<left_size):
        if left[l]>right[r]:
            arr[i]=right[r]
            r=r+1
        else :
            arr[i]=left[l]
            l=l+1
        i=i+1
    #copy remaining elements
    while r<right_size:
        arr[i]=right[r]
        i=i+1
        r=r+1
    while l<left_size:      
        arr[i]=left[l]
        i=i+1
        l=l+1
    return arr       

def merge_sort(arr):
    n=len(arr)
    if n<=1:
        return 
    mid=n//2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    return merge(left_arr,right_arr,arr)
