
#https://github.com/JakubPluta/gymhero
#https://codingnomads.com/python-numpy-course-overview-what-is-numpy#intro

import numpy as np

if __name__ == "__main__":
    a = np.arange(12)
    print("Whet Returns a NumPy View")
    print(a[5:8])
    b = a[5:8]
    print(b)
    # now b is a view of the data in a, so if 
    # we update b, it will update the data in a
    b[0]=50
    print(b)
    print(a)
    print(b.base) 
    # when we print the base of b, 
    # we see it is the original array a
    print(a.base) 
    # this will be None, 
    # since a is the original array
    c = a[a>5]
    print(c)
    print("Whet Returns a NumPy Copy")
    c = a[a>5]
    print(c)
    c[0]=100 
    # this will not update a because c is a copy of a
    print(c)
    print(a)
    print(c.base) 
    # this will be None since c is a copy of a
    # multi dimensional arrays and slicing will return copies
    a = np.arange(12).reshape(3,4)
    print(a)
    b = a[0:2, 0:2]
    print(b)
    print()
    # multiply all elements of b by 2
    b=b*2 
    print(b)
    print()
    # a is not updated since b is a copy of a
    print(a) 
    print(b.base)
    print("How to Make Sure You Return a NumPy Copy")
    a = np.arange(12)
    print(a[5:8])
    # b will be a view of a, but we can force it to copy
    b=a[5:8].copy() 
    print(b)
    print(b.base) # will be None





