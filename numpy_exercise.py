import numpy as np


# Exercise 1

arr = np.array([0,1,2,3,4,5,6,7,8,9])
arr[arr%2==1] = -1
print(arr)


# Exercise 2
a = np.arange(10).reshape(2,5)
print(a)


# Exercise 3
a = np.array([1,2,3])
print(np.r_[np.repeat(a, 3), np.tile(a, 3)])



# Exercise 4

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.intersect1d(a, b))

# Exercise 5
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

print(np.where(a == b))

# Exercise 6

a = np.random.uniform(5,10, size=(5,3))
print(a)

# Exercise 7

np.set_printoptions(threshold=6)
a = np.arange(15)
print(a)


# Exercise 8
np.set_printoptions(suppress=True)
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3

print(rand_arr)


#Exercise 9
arr = np.arange(9).reshape(3,3)
arr[:,[0, 1]] = arr[:,[1, 0]]
print(arr)


# Exercise 10
arr = np.arange(9).reshape(3,3)
arr[[0, 1], :] = arr[[1, 0], :]
print(arr)



