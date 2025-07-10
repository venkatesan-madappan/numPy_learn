
#https://github.com/JakubPluta/gymhero
#https://codingnomads.com/python-numpy-course-overview-what-is-numpy#intro

import numpy as np

'''
https://codingnomads.com/numpy-broadcasting
https://numpy.org/doc/stable/user/basics.broadcasting.html#broadcasting

Broadcasting in NumPy is a set of rules by which ufuncs operate on arrays of different sizes and/or dimensions. 

The general rule is that we compare the two arrays and start from the right side and work our way left. 
If the dimensions are the same or one of the dimensions is 1 then we are good. 
If the dimensions are different and neither is 1 then we can't broadcast and we get an error.

NumPy Broadcasting allows operations between arrays of different shapes by extending smaller arrays to match larger ones.
Broadcasting rules: Start comparing dimensions from the right (last dimension). If dimensions are equal, or one is 1, broadcasting can occur. If they're different and neither is 1, you encounter an error.
Scalars are also broadcasted to match the size of arrays during arithmetic operations.
For arrays with mismatched shapes, reshaping or adding new dimensions can often resolve broadcasting issues.

'''

if __name__ == "__main__":
    print(" NumPy Broadcasting ")
    #NumPy Broadcasting with a Single Number and Array
    a = np.array([1, 2, 3])
    print(a)
    print()
    #this will add 5 to each element of a 
    result = a + 5
    print(result)
    a = np.array([[0.0, 0.0, 0.0],
                 [10.0, 10.0, 10.0],
                 [20.0, 20.0, 20.0],
                 [30.0, 30.0, 30.0]])
    print(a.shape)
    print()

    b = np.array([1.0, 2.0, 3.0])
    print(b.shape)
    # This will add b to each row of a, it works 
    # because b has the same number of columns as a
    print(a+b)

    #Broadcast Two Arrays When Both Must be Stretched
    #Now, note it is possible to broadcast two arrays together when both need to 
    #be "stretched" to match. This is a bit more complicated but here is an example of that.
    # make a into a column vector
    a = np.array([0.0, 10.0, 20.0, 30.0]).reshape(-1,1) 
    print(a) 
    # a is a column vector now
    print(a.shape) 
    print()

    b = np.array([1.0, 2.0, 3.0])
    print(b)   
    # b is a row vector
    print(b.shape) 
    print()

    print(a + b)




