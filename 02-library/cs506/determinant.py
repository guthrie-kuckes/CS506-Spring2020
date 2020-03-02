

def determinant(matrix):
    assert len(matrix) == len(matrix[0])

    if len(matrix) == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    else:
        determinant = 0
        for m in range(0, lem(matrix)):
            sign = -1
            if m % 2 == 0:
                sign = 1
            lesser = 