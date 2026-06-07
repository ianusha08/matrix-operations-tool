```Python
import numpy as np

print("=== Matrix Operations Tool ===")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Matrix A
print("\nEnter values for Matrix A:")
A = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = float(input(f"A[{i+1}][{j+1}]: "))
        row.append(value)
    A.append(row)

# Matrix B
print("\nEnter values for Matrix B:")
B = []
for i in range(rows):
    row = []
    for j in range(cols):
        value = float(input(f"B[{i+1}][{j+1}]: "))
        row.append(value)
    B.append(row)

A = np.array(A)
B = np.array(B)

print("\nMatrix A:")
print(A)

print("\nMatrix B:")
print(B)

print("\nAddition:")
print(A + B)

print("\nSubtraction:")
print(A - B)

print("\nTranspose of A:")
print(A.T)

print("\nDeterminant of A:")
if rows == cols:
    print(np.linalg.det(A))
else:
    print("Determinant can only be calculated for square matrices.")

print("\nMultiplication:")
if cols == rows:
    try:
        print(np.matmul(A, B))
    except:
        print("Multiplication not possible.")
else:
    print("Multiplication not possible for these matrix dimensions.")
```
