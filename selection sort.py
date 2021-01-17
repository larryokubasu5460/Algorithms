# selection sort algorithm
# create a list of elements
L=list()
print("Enter stop to terminate")
while True:
    val=input("Enter elements: ")
    if val == 'stop':
        break
    L.append(val)
print("Elements in List: ",L)
# sort using selection
# change to integer from string
A=[int(item) for item in L]
for i in range(len(A)):
    min=i
    # assign the first index to 
    # advance to next index and scan for minimum
    for j in range(i+1,len(A)):
        if A[j]<A[min]:
            min=j
    # swap the two
    A[i],A[min]=A[min],A[i]

    # print the list
print("Sorted list: ",A)




