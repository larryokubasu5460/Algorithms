# find the smallest distance between a pair of points
import numpy as np
import math
def closest_pair(array):
    result={}
    result['point 1']=array[0]
    result['point 2']=array[1]
    result['distance']=np.sqrt((array[0][0]-array[1][0])**2+(array[0][1]-array[1][1])**2)

    for i in range(len(array)-1):
        for j in range(i+1,len(array)):
            distance=np.sqrt((array[i][0]-array[j][0])**2+(array[i][1]-array[j][1])**2)
            if distance < result['distance']:
                result['point 1']=array[i]
                result['point 2']=array[j]
                result['distance']=distance
    return result

a = [(5, 3), (9, 0), (4, 6), (2, 2), (0, 0),(2, 3), (12, 30), (40, 50), (5, 1), (12, 100), (93, 4)]
print(closest_pair(a))
