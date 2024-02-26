from scipy.linalg import solve
import numpy as np

# Define the matrices and vectors for the first system of equations
A1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
b1 = np.array([2, 12, 10])

# Solve the first system of equations
solution1 = solve(A1, b1)

# Define the matrices and vectors for the second system of equations
A2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
b2 = np.array([2, 12, 21, 37])

# Solve the second system of equations
solution2 = solve(A2, b2)

# Output the solutions
print("Solution for the first system of equations (x1, x2, x3):", solution1)
print("Solution for the second system of equations (x1, x2, x3, x4):", solution2)
