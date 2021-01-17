# this is a divide and conquer algorithm

def merge_sort(array,left,right):
    if left >= right:
        return 
    middle=(left+right)//2
    merge_sort(array,left,middle)
    merge_sort(array,middle+1,right)
    merge(array,left,right,middle)

def merge(array,left,right,middle):
    # make copies
    l_copy=array[left:middle+1]
    r_copy=array[middle+1:right+1]

    # create indices 
    l_index=0
    r_index=0
    sorted_index=left

    # go through both copies and compare
    while l_index <len(l_copy) and r_index < len(r_copy):
        if l_copy[l_index]<= r_copy[r_index]:
            array[sorted_index]=l_copy[l_index]
            l_index=l_index+1

        else:
            array[sorted_index]=r_copy[r_index]
            r_index=r_index+1
# regardless of both advance the sorted array index 
        sorted_index=sorted_index+1

# if any copy runs out advance the remaining copy
    while l_index < len(l_copy):
        array[sorted_index]=l_copy[l_index]
        sorted_index=sorted_index+1
        l_index=l_index+1

    while r_index < len(r_copy):
        array[sorted_index]=r_copy[r_index]
        sorted_index=sorted_index+1
        r_index=r_index+1

array=[100,234,45,3,67,895,32,4,8,67,3,2,4,67,841,34,6]
print("array ",array)
merge_sort(array,0,len(array)-1)
print("Sorted array", array)