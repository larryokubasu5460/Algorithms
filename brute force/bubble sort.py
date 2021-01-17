

def bubble_sort(array):
    for i in range(len(array)-1):
        index=i
        for j in range(i+1,len(array)):
            if array[index]>=array[j]:
                array[index], array[j]=array[j],array[index]

array=[100,234,45,3,67,895,32,4,8,67,3,2,4,67,841,34,6]
print("array ",array)
bubble_sort(array)
print("Sorted array", array)