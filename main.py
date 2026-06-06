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