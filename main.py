import numpy as np

empty_array = np.empty
zeros_array = np.zeros((3,4)) # np.zeros(4) for one dimension
ones_array = np.ones(5) # np.ones((3,4)) for two dimension

print("Empty",empty_array)
print("Zeros",zeros_array)
print("Ones",ones_array)

# random one dimension array takes argument: start_or_stop,stop,step
print("start_or_stop",np.arange(100)) # start_or_stop works like start from zero to 99. why not 100 because end exclude
print("start,stop",np.arange(1,10)) # start,stop from 1 to 9.
print("start,stop,step",np.arange(1,15,2)) # start,stop,step from 1 steps 2: 3,5,7,9,11,13.

# random
print(np.random.randint(30,size=(3,3)))

arr = np.array([[1,2,3],[4,5,6]])

rows,columns = arr.shape

print("Rows",rows)
print("Columns",columns)
print("Shape",arr.shape)
print("Dimension",arr.ndim)
print("Size",arr.size)
print("Dtype",arr.dtype)

numbers = np.array([1,2,3,4,5,6,7,8,9,10])

print("Sum",numbers.sum())
print("Sqrt",np.sqrt(numbers))
print("Mean",numbers.mean())
print("Max",numbers.max())
print("Std",numbers.std())

# vectorization

print(numbers + 10)
print(numbers * 5)

# Broadcasting
print("Broadcasting.......")
print(arr + 10) # numpy handles like this [1,2,3] + [10,10,10] to match the shape.
print(" ")
print(np.array([1,2,3]) + np.array([10,10,10]))

# Boolean mask

mask = numbers >= 5 # return array of boolean

print("Mask",mask)

print(numbers[mask]) # return numbers gte 5

# aggregation

scores = np.array([[90,80,100],[70,65,88]])

sum_of_scores = np.sum(scores)

sum_of_each_student_score = np.sum(scores,axis=1)

print("Sum of scores",sum_of_scores)
print("Sum of each student score",sum_of_each_student_score)

# save and load

np.save("scores.npy",scores)

loaded = np.load("scores.npy")

np.savetxt("scores.csv",scores)
print(np.loadtxt("scores.csv"))

print(loaded)