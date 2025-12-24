import numpy as np

# 1. Create a 4x4 Matrix
# Using arange to generate numbers 1 to 16, then reshaping into 4x4
matrix = np.arange(1, 17).reshape(4, 4)

print("Original Matrix:")
print(matrix)
print("-" * 20)

# 2. Extract the first two rows
# Syntax: [:2] means from start up to (but not including) index 2
first_two_rows = matrix[:2, :]
print("1. First Two Rows:")
print(first_two_rows)
print("-" * 20)

# 3. Extract the first two columns
# Syntax: [:, :2] means all rows (:), and columns from start up to index 2
first_two_cols = matrix[:, :2]
print("2. First Two Columns:")
print(first_two_cols)
print("-" * 20)

# 4. Extract 2x2 submatrix from the center
# Rows: indices 1 to 3 (covers rows 1 and 2)
# Columns: indices 1 to 3 (covers columns 1 and 2)
center_submatrix = matrix[1:3, 1:3]
print("3. Center 2x2 Submatrix:")
print(center_submatrix)