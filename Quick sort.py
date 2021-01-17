# based on the divide and conquer technique
# start with the partitions and choose the first element as the pivot and increment to the next element to scan

def partition(array,start,end):
    pivot=array[start]
    low=start+1
    high=end

    # loop and swap values 
    while True:
        while low<=high and array[high]>=pivot:
            high=high-1

        while low<=high and array[low]<=pivot:
            low=low+1
        
        if low<=high:
            array[high], array[low]=array[low],array[high]
        else:
            break

    array[high],array[start]=array[start],array[high]

    return high

def quick_sort(array,start,end):
    if start>=end:
        return
    p=partition(array,start,end)
    quick_sort(array,start,p-1)
    quick_sort(array,p+1,end)
   

array=[100,234,45,3,67,895,32,4,8,67,3,2,4,67,841,34,6]
print("array ",array)
quick_sort(array,0,len(array)-1)
print("Sorted array", array)