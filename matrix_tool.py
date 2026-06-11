
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

while True:
    print("\n=== Matrix Operations Menu ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        print("\nAddition:")
        print(A + B)

    elif choice == 2:
        print("\nSubtraction:")
        print(A - B)

    elif choice == 3:
        print("\nMultiplication:")
        try:
            print(np.matmul(A, B))
        except ValueError:
            print("Multiplication not possible for these matrix dimensions.")

    elif choice == 4:
        print("\nTranspose of Matrix A:")
        print(A.T)

    elif choice == 5:
        print("\nDeterminant of Matrix A:")
        if rows == cols:
            print(np.linalg.det(A))
        else:
            print("Determinant can only be calculated for square matrices.")

    elif choice == 6:
        print("Exiting Matrix Operations Tool...")
        break

    else:
        print("Invalid choice. Please select a valid option.")
