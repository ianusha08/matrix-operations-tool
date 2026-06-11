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

print("\n=== Matrix Operations Menu ===")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Transpose")
print("5. Determinant")
print("6. Exit")

choice = int(input("\nEnter your choice: "))
