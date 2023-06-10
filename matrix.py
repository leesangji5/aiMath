matA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def sum_of_matrix(mat1, mat2):
    if ((len(mat1) != len(mat2)) and (len(mat1[0]) != len(mat2[0]))):
        print("Error: Matrix size is not same")
        return 0
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] + mat2[i][j])
        result.append(row)
    return result

def minus_of_matrix(mat1, mat2):
    if ((len(mat1) != len(mat2)) and (len(mat1[0]) != len(mat2[0]))):
        print("Error: Matrix size is not same")
        return 0
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat1[0])):
            row.append(mat1[i][j] - mat2[i][j])
        result.append(row)
    return result

def multiply_of_matrix(mat1, mat2):
    if (len(mat1[0]) != len(mat2)):
        print("Error: The number of columns in the first matrix must equal the number of rows in the second matrix.")
        return 0
    result = []
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            a = 0
            for k in range(len(mat1[0])):
                a += mat1[i][k] * mat2[k][j]
            row.append(a)
        result.append(row)

    return result

def print_matrix(mat):
    if (not mat):
        return 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()

def input_matrix():
    row = int(input("Enter the number of rows: "))
    col = int(input("Enter the number of columns: "))
    mat = []
    
    for i in range(row):
        row = []
        response = input("Enter the elements of row ")
        response = response.split(" ")

        if (len(response) != col):
            print("Error: Invalid input")
            return 0
    
        for i in range(col):
            row.append(int(response[i]))
        mat.append(row)
    print_matrix(mat)
    return mat

def main():
    run = True
    mat1 = matA
    mat2 = matB

    while run:
        print("1. Sum of matrix")
        print("2. Minus of matrix")
        print("3. Multiply of matrix")
        print("4. Transpose of matrix")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print_matrix(sum_of_matrix(mat1, mat2))
        elif choice == 2:
            print_matrix(minus_of_matrix(mat1, mat2))
        elif choice == 3:
            print_matrix(multiply_of_matrix(mat1, mat2))
        elif choice == 4:
            mat1 = input_matrix()
            mat2 = input_matrix()
        elif choice == 5:
            run = False
        else: 
            print("Error: Invalid choice")
    return 

if __name__ == "__main__":
    main()