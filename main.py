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

scores = np.array([[97,88],[29,81],[30,78]])
print(scores)

print("Prefix",prefix,"number of dims",prefix.ndim)
print("Numbers ",numbers,"number of dims",numbers.ndim)
print("Scores\n",scores,"\nnumber of dimensions",scores.ndim)
