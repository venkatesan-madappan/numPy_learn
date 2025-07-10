
#https://github.com/JakubPluta/gymhero
#https://codingnomads.com/python-numpy-course-overview-what-is-numpy#intro

import numpy as np

'''
To sort arrays using NumPy sort, use the command np.sort() to return a sorted copy of an array without altering the original.
Use the NumPy argsort command - np.argsort() - to return indices that would sort the array.
array.sort() sorts the array in-place, changing the original array.
Multi-dimensional arrays can be sorted along specific axes using np.sort(a, axis=n). This does not alter the original array.
When sorting multi-dimensional arrays, the axis parameter determines the axis along which the array is sorted. For 2D arrays, axis=0 sorts along the rows (which sorts the columns) while axis=1 sorts along the columns (which sorts the rows).
'''

if __name__ == "__main__":
    print(" Sort Argsort ")
    a = np.array([2, 1, 4 ,3])
    # returns the sorted array (a copy)
    sorted_array = np.sort(a)
    print(sorted_array)
    print(" Argsort ")
    a = np.array([2, 1, 4 ,3])
    # Returns the indices that would sort an array.
    sorted_array = np.argsort(a)
    print(sorted_array)
    #How to Sort Arrays In-Place
    # in-place sorting

    a = np.array([2, 1, 4, 3])
    # sorts a in place, returns nothing
    a.sort() 
    print(a)
    # multi-dimensional sorting

    a = np.array([[14, 11], [12, 13]])
    print(a)
    print()
    # Sort along the first axis
    print(np.sort(a, axis=0))
    print()
    # Sort along the second axis
    print(np.sort(a, axis=1))


