import numpy as np

# 1. Array Creation
# -----------------
print("1. Array Creation")
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
print("1D array:", a)
print("2D array:\n", b)

# Creating arrays filled with zeros, ones, or a constant value
zeros = np.zeros((2, 3))
ones = np.ones((2, 3))
full = np.full((2, 3), 7)
print("Zeros array:\n", zeros)
print("Ones array:\n", ones)
print("Full array with 7:\n", full)

# Creating arrays with ranges
arange_array = np.arange(0, 10, 2)
linspace_array = np.linspace(0, 1, 5)  # 5 evenly spaced values from 0 to 1
print("Range array:", arange_array)
print("Linspace array:", linspace_array)

# Random arrays
rand_array = np.random.random((2, 2))  # random values between 0 and 1
randint_array = np.random.randint(0, 10, (2, 2))  # random integers
print("Random array:\n", rand_array)
print("Random integers array:\n", randint_array)


# 2. Basic Arithmetic Operations
# ------------------------------
print("\n2. Basic Arithmetic Operations")
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("x:", x)
print("y:", y)
print("x + y:", x + y)
print("x - y:", x - y)
print("x * y:", x * y)
print("x / y:", x / y)

# Mathematical functions
print("sin(x):", np.sin(x))
print("cos(x):", np.cos(x))
print("exp(x):", np.exp(x))
print("sqrt(x):", np.sqrt(x))

# Broadcasting
print("\nBroadcasting:")
scalar = 10
print("x + scalar:", x + scalar)
print("x * scalar:", x * scalar)


# 3. Indexing and Slicing
# -----------------------
print("\n3. Indexing and Slicing")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original array:\n", arr)
print("Element at [0, 1]:", arr[0, 1])
print("Slice rows 1 and 2:\n", arr[1:3])
print("Slice columns 1 and 2:\n", arr[:, 1:3])


# 4. Reshaping Arrays
# -------------------
print("\n4. Reshaping Arrays")
reshaped = arr.reshape(1, 9)
flattened = arr.flatten()
print("Reshaped array:\n", reshaped)
print("Flattened array:", flattened)


# 5. Aggregation Functions
# ------------------------
print("\n5. Aggregation Functions")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard Deviation:", np.std(arr))
print("Sum along axis 0 (columns):", np.sum(arr, axis=0))
print("Sum along axis 1 (rows):", np.sum(arr, axis=1))


# 6. Advanced Operations
# ----------------------
print("\n6. Advanced Operations")

# Transpose
print("Transpose of arr:\n", arr.T)

# Dot product
v = np.array([1, 2, 3])
w = np.array([4, 5, 6])
dot_product = np.dot(v, w)
print("Dot product of v and w:", dot_product)

# Matrix multiplication
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
matrix_product = np.matmul(matrix_a, matrix_b)
print("Matrix product:\n", matrix_product)

# Stack arrays vertically and horizontally
stacked_vertical = np.vstack((x, y))
stacked_horizontal = np.hstack((x.reshape(3, 1), y.reshape(3, 1)))
print("Stacked vertically:\n", stacked_vertical)
print("Stacked horizontally:\n", stacked_horizontal)

# Statistical functions on random numbers
random_numbers = np.random.randn(1000)  # 1000 random numbers from a normal distribution
print("Mean of random numbers:", np.mean(random_numbers))
print("Standard deviation of random numbers:", np.std(random_numbers))
print("Minimum:", np.min(random_numbers))
print("Maximum:", np.max(random_numbers))
