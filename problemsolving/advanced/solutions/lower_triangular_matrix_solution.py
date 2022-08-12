# Python3 program to print Lower
# triangular and Upper triangular
# matrix of an array

# Function to form lower triangular
# matrix
def print_lower_triangular_matrix(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if (i < j):
                print("0", end=" ");
            else:
                print(matrix[i][j],
                      end=" ");
        print(" ");


# Function to form upper triangular matrix
def print_matrix(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            print(matrix[i][j],end=" ");
        print(" ");
# Driver Code
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]];
row = 3;
col = 3;

print("Initial matrix: ");
print_matrix(matrix, row, col);

print("Lower triangular matrix: ");
print_lower_triangular_matrix(matrix, row, col);
