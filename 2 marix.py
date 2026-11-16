
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
1
A = []
B = []
C = []

print("Enter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]: ")))
    A.append(row)

print("Enter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[{i}][{j}]: ")))
    B.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(A[i][j] + B[i][j])
    C.append(row)

print("Sum of the two matrices:")
for row in C:
    print(row)
