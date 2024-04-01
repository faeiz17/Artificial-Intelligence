'''Imagine two matrices given in the form of 2D lists as under;
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]
Write a python code that finds another matrix/2D list that is a product of and b, i.e.,
C=a*b'''

import numpy as np 

a = [[1, 0, 0], [0, 1, 0], [0, 0, 1] ]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9] ]

result_matrix = np.dot(a,b)
print("product of matrices: ")
print(result_matrix)