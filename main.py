import numpy as np

# print(np.__version__)

numbers = np.array([1,2,3,4,5,6])
print(numbers)

print("Type",type(numbers))

# squares 
numbers = numbers * 2
print(numbers)

prices = [10,15,11,20]
print(prices)

# concat
prices = prices*2
print(prices)

prefix = np.array(252)

scores = np.array([
    [97,88],
    [29,81],
    [30,78]
    ])

print(scores)

print("Prefix",prefix,"number of dims",prefix.ndim)
print("Numbers ",numbers,"number of dims",numbers.ndim)
print("Scores\n",scores,"\nnumber of dimensions",scores.ndim)

# chain indexing
print(scores[0][0])
print(scores[0][1])
print(scores[1][0])

# get entire row
print(scores[0])

# multi dimensional indexing
print(scores[0,1])
print(scores[1,0])
print(scores[2,0])

# slicing  index 0 then slicing : all | -> first row each all items
print(scores[0,:])

#  index : all and slicing : all | -> all for all
print(scores[:,:])

#  index : all and splicing 0 | -> all row each item index 0
print(scores[:,0])

# copy and view

years = np.array([
    2026,
    1999,
    2000,
    2003,
    2007,
    2014
])

print("Original years",years)
copy_years = years.copy()
print("Copy years",copy_years)
view_years  = years.view()
print("View years",view_years)

years[0]=1998

print("Modified Original years",years)
print("Copy years",copy_years)
print("View years",view_years)

print("Original base",years.base)
print("Copy base",copy_years.base)
print("View base",view_years.base)

one_dim = np.array([1,2,3,4,5,6,7,8])
print(one_dim)
print(one_dim.shape)

two_dim = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(two_dim)
print(two_dim.shape)

re_shaped = one_dim.reshape(4,2)
print(re_shaped)
print(re_shaped.shape)
print(re_shaped.ndim)

print(two_dim.reshape(5,2))

# loop through
print("Looping through")
for x in one_dim:
    print(x)

# for more than one dimension array you must use nested loop to get the value
total_scores = 0
for score in scores:
    print(score)
    for n in score:
        total_scores += n
        print(n)

print("Total",total_scores)

# using numpy iterator to simplify loop of more than one Dimension array
print("Using numpy iterator")
for score in np.nditer(scores):
    print(score)

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([6,7,8,9,10])

arr = np.concatenate((arr1,arr2))
print(arr)

print(np.concatenate((scores,scores),axis=1))

print("Broadcasting..................")

x = np.array([1,2,3,4,5,6])

y = x * 2

print("Y",y)

n1 = np.array([
    [1,2],
    [3,4],
    [5,6]
])

n2 = np.array([30,40])

print("Addition",n1 + n2)
print("Subtraction",n1-n2)
print("Multiplication",n1*n2)
print("Division",n1/n2)


print("Splitting.........")

print(np.array_split(n1,3))

print(np.array_split(x,2))

print("Searching........")

n3 = np.array([
    [1,2],
    [3,4],
    [5,6]
])

print(np.where(x == 2))
print(np.where(x % 2 == 0))
print(np.where(n3%2==1))