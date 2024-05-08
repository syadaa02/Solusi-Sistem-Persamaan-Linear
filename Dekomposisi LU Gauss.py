# Syada Saleha (21120122120011)
# Fungsi untuk melakukan dekomposisi LU
def dekomposisi_lu(mat):
    n = len(mat)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for i in range(n):
        # Membentuk matriks U
        for k in range(i, n):
            sum_upper = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = mat[i][k] - sum_upper

        # Membentuk matriks L
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                sum_lower = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (mat[k][i] - sum_lower) / U[i][i]

    return L, U


# Fungsi untuk melakukan substitusi maju
def substitusi_maju(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = (b[i] - sum)
    return y


# Fungsi untuk melakukan substitusi mundur
def substitusi_mundur(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * x[j]
        x[i] = (y[i] - sum) / U[i][i]
    return x


# Matriks koefisien dan vektor hasil
A = [
    [2, -1, 3],
    [1, 2, -5],
    [3, 1, 1]
]

b = [7, 8, 6]

# Melakukan dekomposisi LU
L, U = dekomposisi_lu(A)

# Menyelesaikan sistem linear dengan substitusi maju dan mundur
y = substitusi_maju(L, b)  # Menyelesaikan L * y = b
x = substitusi_mundur(U, y)  # Menyelesaikan U * x = y

print("Solusi persamaan linear:")
print(x)  # Menampilkan solusi
