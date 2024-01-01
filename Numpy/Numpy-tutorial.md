```python
# ###
# #NUMPY

# #What is Numpy

# - Numpy is a library to manage and perform calculation on n-dimension arrays.
# - Numpy is faster than List
# - Numpy is faster than list because it uses fixed object size. 
# - Advantdages of Numpy 
#     - each integer is 32 bit (4 byte) in numpy (more datatypes are available)
#     - But lists need to store size, reference count, object type and value (can be 8 bytes for 1 number)
#     - Basically numpy uses less bytes of memory 
#     - There is no type checking in numpy (as it uses homogeneous data)
#     - List uses double hops to read data (list stores pointers to the actual object)
#     - Numpy array uses direct reference, it stores data in contiguous memory
#     - Using contiguous memory also helps in better caching 
#     - Both support all ops like insert delete update, but numpy support more features
# - Application of Numpy 
#     - Support mathematics
#     - supported by matplotlib for graph plotting
#     - used for pandas, connect4, etc
#     - Machine learning -> tensors 
```


```python
%pip install numpy
```

    Defaulting to user installation because normal site-packages is not writeable
    Requirement already satisfied: numpy in c:\users\mukul.bindal\appdata\roaming\python\python312\site-packages (1.26.2)
    Note: you may need to restart the kernel to use updated packages.
    

    
    [notice] A new release of pip is available: 23.2.1 -> 23.3.2
    [notice] To update, run: python.exe -m pip install --upgrade pip
    


```python
import numpy as np

# Initialize array 
a = np.array([1, 2, 3])

b = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])

c = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,12,13]], [[14,15,16],[17,18,19]]])

a
b
c
```




    array([[[ 1,  2,  3],
            [ 4,  5,  6]],
    
           [[ 7,  8,  9],
            [11, 12, 13]],
    
           [[14, 15, 16],
            [17, 18, 19]]])




```python
# Get the dimensions
a.ndim, b.ndim, c.ndim
```




    (1, 2, 3)




```python
# Get the shape of the array
a.shape, b.shape, c.shape
```




    ((3,), (2, 4), (3, 2, 3))




```python
# Get datatype
a.dtype
```




    dtype('int32')




```python
# Changing the datatype
a = np.array(a, dtype='float32')
a0 = np.array([1, 2, 3], dtype='int16')
a.dtype, a0.dtype
```




    (dtype('float32'), dtype('int16'))




```python
# Size of one element of array in bytes
a.itemsize, a0.itemsize

```




    (4, 2)




```python
# Number of elements in the array
a.size, b.size, c.size
```




    (3, 8, 18)




```python
# Total memory occupied by the array in bytes
a.itemsize * a.size, c.itemsize * c.size
```




    (12, 72)




```python
# Total memory occupied by the array in bytes
a.nbytes, c.nbytes
```




    (12, 72)



### Accessing / Changing Elements


```python
# Numpy supports a[startindex:endindex:step] to fetch data from [startindex, endindex)  <-- endindex exclusive
# a[row, col] to access a specific element in the 2d - array
# Note that in all below examples, we will use 0 based indexing
```


```python
# Consider below array which is 5*5
a = np.array([[1, 2, 3, 4, 5],[4, 5, 6, 7, 8],[7, 8, 9, 10, 11], [12, 14, 15, 16, 17], [8, 3, 2, 1, 4]])
a
```




    array([[ 1,  2,  3,  4,  5],
           [ 4,  5,  6,  7,  8],
           [ 7,  8,  9, 10, 11],
           [12, 14, 15, 16, 17],
           [ 8,  3,  2,  1,  4]])




```python
# Get 2nd row 3rd column
a[2, 3]
```




    10




```python
# Get all elements of 3rd column
a[:, 3]    # means from all rows, choose 3rd column 
```




    array([ 4,  7, 10, 16,  1])




```python
# Get the 2nd row
a[2, :] # all columns from 2nd row. 
a[2]  # Note that a[2] is same as a[2, :] means if we need all elements in last dimension - no need to specify

```




    array([ 7,  8,  9, 10, 11])




```python
# Get the submatrix starting at 1, 2 and ending at 3, 3
# Means we need to get rows from 1 to 3 inclusive and columns from 2 to 3 inclusive
# For the inclusive index, we need to add 1 to include it
a[1:4, 2:4]
```




    array([[ 6,  7],
           [ 9, 10],
           [15, 16]])




```python
# We can also include steps -
# Get all the elements in 3rd column at even row numbers (0, 2, 4)
a[::2, 3]   # all rows with 2 step, 3rd col
```




    array([ 4, 10,  1])




```python
# For 3-d array we need to use 3 indices -
c[2, 1, 1]
```




    18



### Initializing different types of arrays


```python
# All 0's matrix
np.zeros((2, 3, 4))
```




    array([[[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]],
    
           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]])




```python
np.zeros((2, 3, 4), dtype='float32')
```




    array([[[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]],
    
           [[0., 0., 0., 0.],
            [0., 0., 0., 0.],
            [0., 0., 0., 0.]]], dtype=float32)




```python
#All 1's array
np.ones((3, 4))
```




    array([[1., 1., 1., 1.],
           [1., 1., 1., 1.],
           [1., 1., 1., 1.]])




```python
# Array of a specific number -
# Get array of all 56s
np.full((4, 5), 56, dtype='int32')
# Note that datatype is optional
```




    array([[56, 56, 56, 56, 56],
           [56, 56, 56, 56, 56],
           [56, 56, 56, 56, 56],
           [56, 56, 56, 56, 56]])




```python
# Creating a masking like array
# Suppose we want to create an array of same shape of an existing array, just all 0's or all other kind of elements
np.full(a.shape, 5)
```




    array([[5, 5, 5, 5, 5],
           [5, 5, 5, 5, 5],
           [5, 5, 5, 5, 5],
           [5, 5, 5, 5, 5],
           [5, 5, 5, 5, 5]])




```python
# Inbuilt function
np.full_like(a, 3)
```




    array([[3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3],
           [3, 3, 3, 3, 3]])




```python
# Random decimal numbers
np.random.rand(3, 4)   # Note that we passed normal integer for shape, not a tuple
```




    array([[0.04484643, 0.77568544, 0.7416517 , 0.45596751],
           [0.63927014, 0.55804263, 0.18588722, 0.84125013],
           [0.89329006, 0.22823369, 0.16377902, 0.4112132 ]])




```python
# Creating array from shape of other array
np.random.random_sample(a.shape)
```




    array([[0.87715388, 0.01674094, 0.74357042, 0.50287802, 0.93459749],
           [0.56494741, 0.77808608, 0.41660879, 0.64780419, 0.53756741],
           [0.28277423, 0.18945905, 0.72163711, 0.97031142, 0.82827233],
           [0.93093982, 0.85412736, 0.01969805, 0.92054805, 0.25156018],
           [0.19096279, 0.39563744, 0.626165  , 0.18280718, 0.44410337]])




```python
# Random Integer values
## Need to pass range like params, then size 
# Generate random values of 4x5 with elements in range 0 to 7 exclusive
np.random.randint(7, size=(4, 5))  
```




    array([[6, 1, 1, 2, 3],
           [6, 1, 0, 3, 4],
           [2, 0, 6, 3, 5],
           [0, 1, 1, 0, 1]])




```python
# Get random array of integers of size 5x3 with elements in range -6 to +6 inclusive
np.random.randint(-6, 7, size=(5, 3))
```




    array([[ 5,  2,  6],
           [ 4, -6,  2],
           [-4,  5,  1],
           [ 4,  6, -1],
           [ 1,  4,  6]])




```python
# Generate identity matrix
# Identity matrix of 5*5
np.identity(5)
```




    array([[1., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0.],
           [0., 0., 1., 0., 0.],
           [0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 1.]])




```python
# Creating array from repeated arr / elements
arr = np.array([1, 2, 3])
np.repeat(arr, 3)
```




    array([1, 1, 1, 2, 2, 2, 3, 3, 3])




```python
arr = np.array([[1, 2, 3]])
np.repeat(arr, 3, axis=0)   ## Repeat on 0th axis
```




    array([[1, 2, 3],
           [1, 2, 3],
           [1, 2, 3]])




```python
# Create an array with below data
# 1 1 1 1 1
# 1 0 0 0 1
# 1 0 9 0 1
# 1 0 0 0 1
# 1 1 1 1 1

# Steps:
# - Create 5x5 array with all 1s
# - Create 3x3 array with all 0s
# - make the middle element as 9
# - assign this to the submatrix of 1s array

arr = np.ones((5, 5))
zeros = np.zeros((3, 3))
zeros[1, 1] = 9
arr[1:4, 1:4] = zeros     # Note that we need to mention the entire submatrix
arr
```




    array([[1., 1., 1., 1., 1.],
           [1., 0., 0., 0., 1.],
           [1., 0., 9., 0., 1.],
           [1., 0., 0., 0., 1.],
           [1., 1., 1., 1., 1.]])




```python
# Copy the array
arr = a.copy()
arr
```




    array([[ 1,  2,  3,  4,  5],
           [ 4,  5,  6,  7,  8],
           [ 7,  8,  9, 10, 11],
           [12, 14, 15, 16, 17],
           [ 8,  3,  2,  1,  4]])



### Mathematics


```python
arr = a[:3,:3].copy()
arr
```




    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])




```python
# Using +, -, *, %, ** will perform the operation on all elements
# arr + 3 will add 3 to all elements
# Note that after arithmetic operation , new array will be returned, no change in the original array
```


```python
arr + 3
```




    array([[ 4,  5,  6],
           [ 7,  8,  9],
           [10, 11, 12]])




```python
arr - 3
```




    array([[-2, -1,  0],
           [ 1,  2,  3],
           [ 4,  5,  6]])




```python
arr * 2
```




    array([[ 2,  4,  6],
           [ 8, 10, 12],
           [14, 16, 18]])




```python
arr / 2
```




    array([[0.5, 1. , 1.5],
           [2. , 2.5, 3. ],
           [3.5, 4. , 4.5]])




```python
arr ** 2
```




    array([[ 1,  4,  9],
           [16, 25, 36],
           [49, 64, 81]])




```python
arr % 2
```




    array([[1, 0, 1],
           [0, 1, 0],
           [1, 0, 1]], dtype=int32)




```python
Array operations -
    Using arithmetic operations on two similar arrays will perform the element wise mathematics

brr = a[1:4, 1:4].copy()
arr, brr
```




    (array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]),
     array([[ 5,  6,  7],
            [ 8,  9, 10],
            [14, 15, 16]]))




```python
arr + brr
```




    array([[ 6,  8, 10],
           [12, 14, 16],
           [21, 23, 25]])




```python
brr - arr
```




    array([[4, 4, 4],
           [4, 4, 4],
           [7, 7, 7]])




```python
arr * brr
```




    array([[  5,  12,  21],
           [ 32,  45,  60],
           [ 98, 120, 144]])




```python
crr = a[1:4, 4].copy()
arr, crr
```




    (array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]),
     array([ 8, 11, 17]))




```python
arr + crr     ## Adds the crr row in all the rows of arr
```




    array([[ 9, 13, 20],
           [12, 16, 23],
           [15, 19, 26]])




```python
drr = a[1:4, 3:4].copy()
arr, drr
```




    (array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]),
     array([[ 7],
            [10],
            [16]]))




```python
arr + drr    # drr is a column, so all the colums of arr will be added by drr
```




    array([[ 8,  9, 10],
           [14, 15, 16],
           [23, 24, 25]])




```python
# maths with odd shape - Note that only logically correct operations can be performed
p = arr.copy()
q = a[1:4, 2:4].copy()
p, q
```




    (array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]),
     array([[ 6,  7],
            [ 9, 10],
            [15, 16]]))




```python
p + q   # This operation is not logical, hence invalid, if one axis has same size, other should be either same, or 1
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[82], line 1
    ----> 1 p + q
    

    ValueError: operands could not be broadcast together with shapes (3,3) (3,2) 



```python
# sin, cosine etc
np.sin(arr)
```




    array([[ 0.84147098,  0.90929743,  0.14112001],
           [-0.7568025 , -0.95892427, -0.2794155 ],
           [ 0.6569866 ,  0.98935825,  0.41211849]])




```python
np.cos(arr)
```




    array([[ 0.54030231, -0.41614684, -0.9899925 ],
           [-0.65364362,  0.28366219,  0.96017029],
           [ 0.75390225, -0.14550003, -0.91113026]])




```python
np.tan(arr)
```




    array([[ 1.55740772, -2.18503986, -0.14254654],
           [ 1.15782128, -3.38051501, -0.29100619],
           [ 0.87144798, -6.79971146, -0.45231566]])



### Linear Algebra 


```python
# Performing dot product
# Note that col of first matrix should be equal to rows of second matrix

p = np.array([[1, 2, 4], [2, 4, 3]])
q = np.array([[1, 2], [4, 2], [4, 3]])
p, q
```




    (array([[1, 2, 4],
            [2, 4, 3]]),
     array([[1, 2],
            [4, 2],
            [4, 3]]))




```python
r = p.dot(q)
r
```




    array([[25, 18],
           [30, 21]])




```python
# Compute determinant of square matrix
np.linalg.det(r)
```




    -15.0



### Statistics


```python
stats = np.array([[1, 2, 4], [4, 5, 6]])
stats

```




    array([[1, 2, 4],
           [4, 5, 6]])




```python
# Min / Max of whole matrix
np.min(stats), np.max(stats)  
```




    (1, 6)




```python
# Min of array column wise
np.min(stats, axis = 0)
```




    array([1, 2, 4])




```python
# Max of array, column wise
np.max(stats, axis=0)
```




    array([4, 5, 6])




```python
# Max of array, row wise
np.max(stats, axis=1)
```




    array([4, 6])




```python
# Sum of whole array
np.sum(stats)

```




    22




```python
# Column wise sum
np.sum(stats, axis=0)
```




    array([ 5,  7, 10])



### Re-organizing the arrays


```python
p, q
```




    (array([[1, 2, 4],
            [2, 4, 3]]),
     array([[1, 2],
            [4, 2],
            [4, 3]]))




```python
p.shape
```




    (2, 3)




```python
# Convert p to a 3 x 2 array
# We can reshape the array into any size, any dimension as long as all the elements fit
# Example - 6 elements can fit in 1x6, 6x1, 2x3, 3x2, 1x1x6, 2x3x1 ... so on sizes
p.reshape((3, 2))
```




    array([[1, 2],
           [4, 2],
           [4, 3]])




```python
p.reshape((1, 2, 3))
```




    array([[[1, 2, 4],
            [2, 4, 3]]])




```python
# Vertically stacking vectors
# In Vertical stacks, number of columns should always match
v1 = np.array([1, 2, 4, 5])
v2 = np.array([2, 3, 6, 7])

np.vstack((v1, v2))

```




    array([[1, 2, 4, 5],
           [2, 3, 6, 7]])




```python
np.vstack((v1, v2, v1, v2))
```




    array([[1, 2, 4, 5],
           [2, 3, 6, 7],
           [1, 2, 4, 5],
           [2, 3, 6, 7]])




```python
v1 = np.array([[3, 4, 5],[1, 3, 5]])
v2 = np.array([[5, 3, 8],[7, 1, 4]])
v1, v2, np.vstack((v1, v2))

```




    (array([[3, 4, 5],
            [1, 3, 5]]),
     array([[5, 3, 8],
            [7, 1, 4]]),
     array([[3, 4, 5],
            [1, 3, 5],
            [5, 3, 8],
            [7, 1, 4]]))




```python
# Horizontal stack -
# In horizontal stack, the number of rows should match
h1 = np.array([[1, 2, 4], [7, 9, 0]])
h2 = np.array([[3,5], [8,2]])

h1, h2, np.hstack((h1, h2))
```




    (array([[1, 2, 4],
            [7, 9, 0]]),
     array([[3, 5],
            [8, 2]]),
     array([[1, 2, 4, 3, 5],
            [7, 9, 0, 8, 2]]))



### Miscelleneous


```python
# Create a file (Doing this so that it can run anywhere and not dependent on a file)
import random
random.randint(1, 100)
data = ''
n, m = (7, 8)
for i in range(n):
    for j in range(m):
        data += str(random.randint(1, 100)) + (',' if j<m-1 else '')
    data += '\n'
print(data)
with open('data.csv', 'w') as file:
    file.write(data)
```

    31,81,25,51,47,75,80,56
    4,71,15,92,21,65,63,39
    7,77,16,92,73,25,19,53
    13,53,54,96,88,77,51,96
    80,8,75,83,43,43,95,98
    12,51,68,67,63,47,75,15
    70,20,25,7,74,43,74,3
    
    


```python
# Reading data from a file and converting to np array
filedata = np.genfromtxt('data.csv', delimiter=',')
filedata
```




    array([[31., 81., 25., 51., 47., 75., 80., 56.],
           [ 4., 71., 15., 92., 21., 65., 63., 39.],
           [ 7., 77., 16., 92., 73., 25., 19., 53.],
           [13., 53., 54., 96., 88., 77., 51., 96.],
           [80.,  8., 75., 83., 43., 43., 95., 98.],
           [12., 51., 68., 67., 63., 47., 75., 15.],
           [70., 20., 25.,  7., 74., 43., 74.,  3.]])




```python
# Changing the datatype
filedata.astype('int16')
```




    array([[31, 81, 25, 51, 47, 75, 80, 56],
           [ 4, 71, 15, 92, 21, 65, 63, 39],
           [ 7, 77, 16, 92, 73, 25, 19, 53],
           [13, 53, 54, 96, 88, 77, 51, 96],
           [80,  8, 75, 83, 43, 43, 95, 98],
           [12, 51, 68, 67, 63, 47, 75, 15],
           [70, 20, 25,  7, 74, 43, 74,  3]], dtype=int16)




```python
# Advanced indexing
```


```python
# We can index the elements using a list
# Get the 1st, 2nd, 5th and 6th row from the array
filedata[[1, 2, 5, 6]]    # returns the 1,2,5,6 row
```




    array([[ 4., 71., 15., 92., 21., 65., 63., 39.],
           [ 7., 77., 16., 92., 73., 25., 19., 53.],
           [12., 51., 68., 67., 63., 47., 75., 15.],
           [70., 20., 25.,  7., 74., 43., 74.,  3.]])




```python
# Get the 1, 2, 5, 6th columns from the array
filedata[:, [1, 2, 5, 6]]
```




    array([[81., 25., 75., 80.],
           [71., 15., 65., 63.],
           [77., 16., 25., 19.],
           [53., 54., 77., 51.],
           [ 8., 75., 43., 95.],
           [51., 68., 47., 75.],
           [20., 25., 43., 74.]])




```python
# Boolean matrix where elements > 50
filedata > 50
```




    array([[False,  True, False,  True, False,  True,  True,  True],
           [False,  True, False,  True, False,  True,  True, False],
           [False,  True, False,  True,  True, False, False,  True],
           [False,  True,  True,  True,  True,  True,  True,  True],
           [ True, False,  True,  True, False, False,  True,  True],
           [False,  True,  True,  True,  True, False,  True, False],
           [ True, False, False, False,  True, False,  True, False]])




```python
#Get the matrix where elements are > 50
filedata[filedata>50]
```




    array([81., 51., 75., 80., 56., 71., 92., 65., 63., 77., 92., 73., 53.,
           53., 54., 96., 88., 77., 51., 96., 80., 75., 83., 95., 98., 51.,
           68., 67., 63., 75., 70., 74., 74.])




```python
# If we pass a list or list of list of boolean/0/1 into the array, it will flatten the list using the boolean/0/1 present at those indexes
# Get elements which are even
filedata%2==0
```




    array([[False, False, False, False, False, False,  True,  True],
           [ True, False, False,  True, False, False, False, False],
           [False, False,  True,  True, False, False, False, False],
           [False, False,  True,  True,  True, False, False,  True],
           [ True,  True, False, False, False, False, False,  True],
           [ True, False,  True, False, False, False, False, False],
           [ True,  True, False, False,  True, False,  True, False]])




```python
filedata[filedata%2==0]
```




    array([80., 56.,  4., 92., 16., 92., 54., 96., 88., 96., 80.,  8., 98.,
           12., 68., 70., 20., 74., 74.])




```python
filedata%2==0
```




    array([[False, False, False, False, False, False,  True,  True],
           [ True, False, False,  True, False, False, False, False],
           [False, False,  True,  True, False, False, False, False],
           [False, False,  True,  True,  True, False, False,  True],
           [ True,  True, False, False, False, False, False,  True],
           [ True, False,  True, False, False, False, False, False],
           [ True,  True, False, False,  True, False,  True, False]])




```python
filedata * (filedata%2==0)   ## Puts 0 where this condition is false
```




    array([[ 0.,  0.,  0.,  0.,  0.,  0., 80., 56.],
           [ 4.,  0.,  0., 92.,  0.,  0.,  0.,  0.],
           [ 0.,  0., 16., 92.,  0.,  0.,  0.,  0.],
           [ 0.,  0., 54., 96., 88.,  0.,  0., 96.],
           [80.,  8.,  0.,  0.,  0.,  0.,  0., 98.],
           [12.,  0., 68.,  0.,  0.,  0.,  0.,  0.],
           [70., 20.,  0.,  0., 74.,  0., 74.,  0.]])




```python
((filedata > 50) & (filedata < 100))
```




    array([[False,  True, False,  True, False,  True,  True,  True],
           [False,  True, False,  True, False,  True,  True, False],
           [False,  True, False,  True,  True, False, False,  True],
           [False,  True,  True,  True,  True,  True,  True,  True],
           [ True, False,  True,  True, False, False,  True,  True],
           [False,  True,  True,  True,  True, False,  True, False],
           [ True, False, False, False,  True, False,  True, False]])




```python
filedata * ((filedata > 50) & (filedata < 100))
```




    array([[ 0., 81.,  0., 51.,  0., 75., 80., 56.],
           [ 0., 71.,  0., 92.,  0., 65., 63.,  0.],
           [ 0., 77.,  0., 92., 73.,  0.,  0., 53.],
           [ 0., 53., 54., 96., 88., 77., 51., 96.],
           [80.,  0., 75., 83.,  0.,  0., 95., 98.],
           [ 0., 51., 68., 67., 63.,  0., 75.,  0.],
           [70.,  0.,  0.,  0., 74.,  0., 74.,  0.]])




```python
# Checking if a condtion is true in any or all elements
# Check if all elements are odd
np.all(filedata % 2 == 0)
```




    False




```python
# All elements less than 100?
np.all(filedata < 100)
```




    True




```python
# Any element is divisible by 3?
np.any(filedata % 3 == 0)
```




    True




```python
#creating the diagonal matrix
temp = filedata[:5, :5].copy()
mask = [list([False for i in range(5)]) for i in range(5)]
for i in range(5):
    for j in range(5):
        if i==j:
            mask[i][j] = True
mask = [list([False for i in range(5)]) for i in range(5)]
temp[mask]   # returns the array with the diagonal elements

```




    array([], dtype=float64)




```python
temp * mask    # Returns the masked array
```




    array([[31.,  0.,  0.,  0.,  0.],
           [ 0., 71.,  0.,  0.,  0.],
           [ 0.,  0., 16.,  0.,  0.],
           [ 0.,  0.,  0., 96.,  0.],
           [ 0.,  0.,  0.,  0., 43.]])




```python

```


```python

```
