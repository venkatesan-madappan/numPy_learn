
#https://github.com/JakubPluta/gymhero
#https://codingnomads.com/python-numpy-course-overview-what-is-numpy#intro

import numpy as np

if __name__ == "__main__":
    print(" vstack, hstack, concatenate ")
    print("VSTACK")
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    print(a)
    print(b)
    print(a.shape)
    print(b.shape)
    c = np.vstack((a, b))
    print(c)

    a = np.array([[1], [2], [3]])
    b = np.array([[4], [5], [6]])
    # a = np.squeeze(a) Just a trial
    # b = np.squeeze(b) Just a trial
    print(a)
    print(b)
    print(a.shape)
    print(b.shape)
    c = np.vstack((a, b))
    print(c)

    print("HSTACK")
    a = np.array([[1], [2], [3]])
    b = np.array([[4], [5], [6]])
    print(a)
    print(b)
    print(a.shape)
    print(b.shape)
    c = np.hstack((a, b))
    print(c)

    print("CONCATENATE")

    # np.concatenate can be used to stack arrays 
    # horizontally or vertically
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6]])
    # we specificy along the 0th axis, 
    # which is the vertical axis
    c = np.concatenate((a, b), axis=0) 
    print(c)
    print(a.shape)
    print(b.shape)
    #we specificy along the 1th axis, which is the horizontal axis
    # np.concatenate((a, b), axis=1) 
    # this gives us an error, because the arrays do not 
    # have the same number of dimensions, there are two 
    # rows in a, but only one row in b 
    # so they cannot be stacked horizontally
    # we flip b so that it has two rows, 
    # and then we can stack them horizontally
    c = np.concatenate((a, b.T), axis=1) 
    print(c)
    # if you don't specify the axis, np will flatten 
    # the arrays and stack them horizontally
    c = np.concatenate((a, b), axis=None)
    print(c)
    

