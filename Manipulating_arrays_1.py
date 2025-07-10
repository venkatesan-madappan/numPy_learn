
#https://github.com/JakubPluta/gymhero
#https://codingnomads.com/python-numpy-course-overview-what-is-numpy#intro

import numpy as np

if __name__ == "__main__":
    print(" Reshape, flatten, ravel, newaxis, squeeze")
    a = np.arange(1, 11).reshape(2, 5)
    print(a)
    a = a.reshape(1,10)
    print(a)
    a = np.arange(100)
    print(a.reshape(10, 10))
    print()
    #print(a.reshape(4, 5, 5))
    # We can use -1 once in the reshape function and 
    # numpy will infer what it should be
    print(a.reshape(-1, 5, 5)) 
    print(a.reshape(10, -1)) 
#print(a.reshape(4, -1, -1))  This is not allowed and get an error
#.flatten() will flatten an array into a 1D array and return a copy of
#           the array. It is guaranteed to be contiguous in memory.
#.ravel() will flatten an array into a 1D array and return a view when 
# possible while guaranteeing that the resulting array will be contiguous in memory.
#.reshape(-1) will flatten an array into a 1D array and return a view (when possible)
#  with no guarantee that the resulting array will be contiguous in memory.
    a = np.arange(9).reshape(3,3)
    print(a)
    print()
    print(a.ravel())
    print(a.flatten())
    print(a.reshape(-1))
    c = a.flatten() #returns a copy
    print(f"the base of c is: {c.base}")

    b = a.ravel() # returns a view
    print(f"the base of b is: {b.base}")

    d = a.reshape(-1) # returns a view
    print(f"the base of d is: {d.base}")
#Adding a Dimension With np.newaxis
    a = np.arange(9)
    print(a)
    print(a.shape)
    print()

    ##add one dimension to 'a'
    b = a[:, np.newaxis] ##np.newaxis is an alias for None, it's just more readable
    c = a[:, None] #exactly the same as the above. but you should not do this.

    print(b)
    print(b.shape)
    print()
    print(c)
    print(c.shape)

    #Adding Dimension with np.reshape and expand_dims
    a = np.arange(9)
    print(a)
    print(a.shape)
    print()

    # adds an axis at the end same as a[:, np.newaxis]
    a1 = a.reshape(-1,1) 
    print(a1)
    print(a1.shape)

    print()

    # adds an axis at the beginning, same as a[np.newaxis, :]
    a2 = a.reshape(1,-1) 
    print(a2)
    print(a2.shape)

    # this is how you can use np.expand_dims 
    # to add an axis at the end
    a3 = np.expand_dims(a, axis=-1) 
    print(a3)
    print(a3.shape)
    print()

    # this is how you can use np.expand_dims to 
    # add an axis at the beginning
    a4 = np.expand_dims(a, axis=0)
    print(a4)
    print(a4.shape)
    print()

    # you can use np.expand_dims to add multiple axis 
    # adds two dimensions
    print("Expand dims")
    print(a)
    a5 = np.expand_dims(a, axis=(1,2)) 
    print(a5)
    print(a5.shape)
    print()
    # with np.expand_dims, you can add the axis anywhere you want. 
    # np will automatically figure out where to place your current 
    # axis relative to the requested new ones
    print(a.shape)
    a6= np.expand_dims(a, axis=(0,2)) 
    # add the axis at the beginning 
    # and the end, and the existing values are in the middle
    print(a6.shape)
    # np.squeeze() = operation to undo the addition of placeholder axes
    print(a6.shape)
    a7 = np.squeeze(a6)
    print(a7.shape)












