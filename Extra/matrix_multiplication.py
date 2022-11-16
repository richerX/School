def matrix_multiplication(A, B):
    
    Length_A = len(A)
    if Length_A:
        Width_A = len(A[0])
        for string in A:
            if len(string) != Width_A:
                return "Can't do multiplication, cause of first element isn't matrix"
    else:
        return "Can't do multiplication, cause of first matrix is empty"
    
    Length_B = len(B)
    if Length_B:
        Width_B = len(B[0])
        for string in B:
            if len(string) != Width_B:
                return "Can't do multiplication, cause of second element isn't matrix"
    else:
        return "Can't do multiplication, cause of second matrix is empty"
    
    if Width_A == Length_B:
        result = [[0 for i in range (Width_B)] for j in range(Length_A)]
        for i in range(Length_A):
            for j in range(Width_B):
                for k in range(Width_A):  # Width_A == Length_B
                    result[i][j] += A[i][k] * B[k][j]
        return result
    else:
        return "Can't do multiplication, cause of Width_A != Length_B. Such multiplication of matrix isn't definited!"


X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

answer = Matrix_multiplication(X, Y)

if type(answer) == str:
    print(answer)
elif type(answer) == list:
    for string in answer:
        print(*string)
else:
    print("Type =", type(answer))
    print(answer)
