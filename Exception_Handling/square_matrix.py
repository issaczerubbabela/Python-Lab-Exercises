# Program to print an exception if the input matrix is not a square matrix.
# Print the sum of the upper and lower triangular matrix if the matrix is square.

try:
    upper=0;lower=0
    rows, columns = int(input("Enter no. of rows: ")), int(input("Enter no. of columns: "))
    matrix = [[0 for _ in range(columns)] for _ in range(rows)]
    if rows != columns: raise IndexError
    else:
        for i in range(rows):
            for j in range(columns):
                print("Enter the element in ",i+1,"th row and ",j+1,"th column: ",end='',sep='')
                matrix[i][j] = int(input())
                if(i<j): upper+=matrix[i][j]
                if(j<i): lower+=matrix[i][j]
    print("Sum of lower triangular matrix elements:",lower)
    print("Sum of upper triangular matrix elements:",upper)
    print("Input Matrix:")
    print(matrix)
    for i in matrix:
        print(i)
except IndexError:
    print("The matrix is not Square.")
