# 10.  Given a 2D list (matrix), write a function to transpose the matrix (swap rows and columns).


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])  # Assumes a non-empty matrix with consistent row lengths

    # Create a new matrix for the transpose with swapped dimensions
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Iterate through the original matrix and fill the transposed matrix
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Example usage:
original_matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transposed = transpose_matrix(original_matrix)
print(transposed)
# Expected output: [[1, 4], [2, 5], [3, 6]]