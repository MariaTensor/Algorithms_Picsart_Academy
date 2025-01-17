def matrix_multiplication(A,B,C,n):
    if n == 1:
        C[0][0] += A[0][0] * B[0][0]
    
    mid = n//2
    A11, A12, A21,A22 = divide_matrix(A,mid)
    B11, B12, B21,B22 = divide_matrix(B,mid)
    C11, C12, C21,C22 = divide_matrix(C,mid)

    
    matrix_multiplication(A11, B11, C11, mid)
    matrix_multiplication(A12, B21, C11, mid)

    matrix_multiplication(A11, B12, C12, mid)
    matrix_multiplication(A12, B22, C12, mid)

    matrix_multiplication(A21, B11, C21, mid)
    matrix_multiplication(A22, B21, C21, mid)

    matrix_multiplication(A21, B12, C22, mid)
    matrix_multiplication(A22, B22, C22, mid)





def divide_matrix(M, mid):
    M11 = [row[:mid] for row in M[:mid]]
    M12 = [row[mid:] for row in M[:mid]]
    M21 = [row[:mid] for row in M[mid:]]
    M22 = [row[mid:] for row in M[mid:]]
    return M11, M12, M21, M22
