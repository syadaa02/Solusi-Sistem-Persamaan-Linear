# Syada Saleha (21120122120011)
# Fungsi untuk menghitung determinan matriks
def determinan(mat):
    if len(mat) == 2 and len(mat[0]) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    determinant = 0
    # Loop untuk menghitung determinan menggunakan metode minor
    for c in range(len(mat[0])):
        minor = minor_matriks(mat, 0, c)
        determinant += ((-1) ** c) * mat[0][c] * determinan(minor)  # pastikan ini mendefinisikan variabel dengan benar
    return determinant

# Fungsi untuk mengambil minor dari matriks
def minor_matriks(mat, i, j):
    return [row[:j] + row[j + 1:] for row in (mat[:i] + mat[i + 1:])]  # pastikan 'row' didefinisikan dalam loop

# Fungsi untuk menghitung transpose matriks
def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

# Fungsi untuk mengalikan matriks dengan vektor
def multiply_matrix_vector(mat, vec):
    result = []
    for row in mat:
        result.append(sum(row[i] * vec[i] for i in range(len(vec))))
    return result

# Fungsi untuk menghitung inversi matriks
def inversi_matriks(mat):
    det = determinan(mat)  # pastikan 'det' didefinisikan
    if det == 0:
        raise ValueError("Matriks singular, tidak dapat dihitung inversinya.")

    cofactors = []
    for r in range(len(mat)):
        cofactor_row = []
        for c in range(len(mat[0])):
            minor = minor_matriks(mat, r, c)  # pastikan 'minor' didefinisikan
            cofactor_row.append(((-1) ** (r + c)) * determinan(minor))  # pastikan 'cofactor_row' didefinisikan
        cofactors.append(cofactor_row)

    adjugate = transpose(cofactors)
    inversi = [[adjugate[r][c] / det for c in range(len(adjugate[r]))] for r in range(len(adjugate))]
    
    return inversi

# Fungsi untuk menyelesaikan sistem persamaan linear dengan metode matriks balikan
def solve_with_inverse(A, b):
    A_inv = inversi_matriks(A)  # pastikan 'A_inv' didefinisikan
    x = multiply_matrix_vector(A_inv, b)  # pastikan 'x' didefinisikan
    return x

# Contoh matriks dan vektor
A = [
    [2, -1, 3],
    [1, 2, -1],
    [3, 0, 2]
]

b = [5, 3, 7]

# Menyelesaikan sistem persamaan linear
try:
    solusi = solve_with_inverse(A, b)
    print("Solusi untuk sistem persamaan linear (Metode Matriks Balikan):")
    print(solusi)
except Exception as e:
    print("Error:", e)  # pastikan 'e' didefinisikan
