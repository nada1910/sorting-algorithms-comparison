def bubble_sort(arr): 
    n=len(arr)
    for i in range (n-1):
        sorted=False
        for j in range (n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                sorted=True
        if not sorted:
             break
                
    return arr
               
