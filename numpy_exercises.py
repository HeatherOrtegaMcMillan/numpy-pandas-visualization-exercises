### numpy exercises ### 
import numpy as np


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# 1. How many negative numbers are there? 
    
a[a < 0]
    # output: array([-2, -1, -6, -7])
a[a < 0].shape
    # output : 4


# 2. How many positive numbers are there?
a[a > 0]
    # Output: array([ 4, 10, 12, 23,  3])
a[a > 0].shape
    #  Output: 5

# 3. How many even positive numbers are there?
pos_num = a[a > 0]
pos_num[pos_num % 2 ==0]
    # Out: array([ 4, 10, 12])
pos_num[pos_num % 2 ==0].shape
    # Out: 3

# another way to do it (From Zach's solutions)
positive_mask = a > 0
even_mask = a % 2 == 0
a[positive_mask & even_mask].shape[0]
# Or...
positives = a[a > 0]
positive_evens = positives[positives % 2 == 0]

# 4. If you were to add 3 to each data point, how many positive numbers would there be?
plus3 = a + 3
plus3[plus3 > 0].shape
    # Out: (10,)
# OR #
(a+3)[a+3 > 0]
(a+3)[a+3 > 0].shape

# 5. If you squared each number, what would the new mean and standard deviation be?

squared = [a ** 2]
    # Out: [array([ 16, 100, 144, 529,   4,   1,   0,   0,   0,  36,   9,  49])]
squared[0].mean()
    # Out: 74.0

# 6. A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. 

centered = a - a.mean()
    # Out: array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])

# 7. Calculate the z-score for each data point. 
# Recall that the z-score is given by:
z_score = centered / a.std()
# # array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
#        -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
#         0.        , -1.24034735])

## OR ## 
(a - a.mean()) / a.std()

######################  Extra Numpy Exercises ########################
## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a) #55

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a) # 1

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a) # 10

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = sum_of_a / len(a) # 5.5

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = 1
for n in a:
    product_of_a = product_of_a * n
print(product_of_a)
# Out[22]: 3628800

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = [num ** 2 for num in a]
    # out: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = [num for num in a if num % 2 != 0]
    # out: [1, 3, 5, 7, 9]

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = [n for n in a if n % 2 == 0]
    # [2, 4, 6, 8, 10]

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

## it would take a lot of looping and nested loops

product_of_b = 1
for x in b:
    for y in x:
        product_of_b = product_of_b * y
    # 20160
list_o_squares_b = [num ** 2 for l in b for num in l]
    # [9, 16, 25, 36, 49, 64]

# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array(b)

sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

sum_of_b = np.sum(b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])

min_of_b = np.min(b)
## OR min_of_b = b.min() <----- WHY? only works when b is numpy array

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = np.max(b)
## or max_of_b = b.max()

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = np.mean(b)

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = np.product(b)       

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b ** 2
# array([[ 9, 16, 25],
#        [36, 49, 64]])

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 != 0]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
evens_in_b = b[b % 2 == 0]

# Exercise 9 - print out the shape of the array b.
print(b.shape)
    # (2, 3)

# Exercise 10 - transpose the array b.
np.transpose(b)
    # array([[3, 6],
    #        [4, 7],
    #        [5, 8]])

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b.reshape(1,6)
    # array([[3, 4, 5, 6, 7, 8]])

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b.reshape(6,1) # What's the difference between this and .reshape(6, -1) is -1 an autofill? 
    # array([[3],
    #        [4],
    #        [5],
    #        [6],
    #        [7],
    #        [8]])

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

c = np.array(c)
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = np.min(c) #1 
max_of_c = np.max(c) #9
sum_of_c = np.sum(c) #45
product_of_c = np.product(c) #362880
#same thing here, all these can be flipped to c.numpyfunction() because we converted it to a numpy array

# Exercise 2 - Determine the standard deviation of c.
np.std(c) #2.581988897471611

# Exercise 3 - Determine the variance of c.
np.var(c) # 6.66667

# Exercise 4 - Print out the shape of the array c
c.shape # (3,3)

# Exercise 5 - Transpose c and print out transposed result.
print(np.transpose(c))
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

# Exercise 6 - Get the dot product of the array c with c. 
np.dot(c, c)
    # array([[ 30,  36,  42],
    #        [ 66,  81,  96],
    #        [102, 126, 150]])

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
np.sum(c * np.transpose(c))
# can also do (c * np.transpose(c)).sum()

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

# i used product spelled all the way out and it worked

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

d = np.array(d)

# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)
    # array([[ 0.89399666, -0.98803162,  0.85090352,  0.        ,  0.58061118,
    #     -0.80115264],
    #    [ 0.85090352, -0.89399666,  0.98803162, -0.17604595,  0.89399666,
    #      0.        ],
    #    [-0.30481062,  0.85090352, -0.85090352,  0.89399666, -0.85090352,
    #     -0.80115264]])

# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)
    # array([[-0.44807362,  0.15425145,  0.52532199,  1.        ,  0.81418097,
    #     -0.59846007],
    #    [ 0.52532199, -0.44807362,  0.15425145,  0.98438195, -0.44807362,
    #      1.        ],
    #    [-0.95241298,  0.52532199,  0.52532199, -0.44807362,  0.52532199,
    #     -0.59846007]])

# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)
    # array([[-1.99520041, -6.4053312 ,  1.61977519,  0.        ,  0.71312301,
    #      1.33869021],
    #    [ 1.61977519,  1.99520041,  6.4053312 , -0.17883906, -1.99520041,
    #      0.        ],
    #    [ 0.32004039,  1.61977519, -1.61977519, -1.99520041, -1.61977519,
    #      1.33869021]])

# Exercise 4 - Find all the negative numbers in d
d[d < 0]
    #([-90, -30, -45, -45])

# Exercise 5 - Find all the positive numbers in d
d[d > 0]
    #90,  30,  45, 120, 180,  45, 270,  90,  60,  45,  90, 180

# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d) 
    #[-90, -45, -30,   0,  30,  45,  60,  90, 120, 180, 270])

# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))
    # 11

# Exercise 8 - Print out the shape of d.
d.shape
# (3, 6)

# Exercise 9 - Transpose and then print out the shape of d.
np.transpose(d).shape 
# or d.transpose().shape
# (6, 3)

# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9, 2))
# or d.reshape(9,2)

    # array([[ 90,  30],
    #        [ 45,   0],
    #        [120, 180],
    #        [ 45, -90],
    #        [-30, 270],
    #        [ 90,   0],
    #        [ 60,  45],
    #        [-45,  90],
    #        [-45, 180]])


