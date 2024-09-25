def rotate_2d_matrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row to get the 90 degree clockwise rotation
    for i in range(n):
        matrix[i].reverse()
