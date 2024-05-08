# Syada Saleha (21120122120011)
# Fungsi untuk melakukan dekomposisi Crout
def dekomposisi_crout(mat):
    n = len(mat)
    L = [[0] * n for _ in range(n)]
    U = [[0] * n for _ in range(n)]

    for j in range(n):
        # Membentuk matriks U
        for i in range(j):
            sum_upper = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = (mat[i][j] - sum_upper) / L[i][i]
        
        # Membentuk matriks L
        for i in range(j, n):
            sum_lower = sum(L[i][k] * U[k][j] for k in range(j))
            L[i][j] = mat[i][j] - sum_lower
        
        # Set U[j][j] = 1 untuk elemen diagonal utama
        U[j][j] = 1

    return L, U


# Fungsi untuk melakukan substitusi maju
def substitusi_maju(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        sum = 0
        for j in range(i):
            sum += L[i][j] * y[j]
        y[i] = (b[i] - sum) / L[i][i]
    return y


# Fungsi untuk melakukan substitusi mundur
def substitusi_mundur(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        sum = 0
        for j in range(i + 1, n):
            sum += U[i][j] * x[j]
        x[i] = y[i] - sum
    return x


# Matriks koefisien dan vektor hasil
A = [
    [2, -1, 3],
    [1, 2, -1],
    [3, 1, 1]
]

b = [7, 8, 6]

# Melakukan dekomposisi Crout
L, U = dekomposisi_crout(A)

# Menyelesaikan sistem linear dengan substitusi maju dan mundur
y = substitusi_maju(L, b)  # Menyelesaikan L * y = b
x = substitusi_mundur(U, y)  # Menyelesaikan U * x = y

print("Solusi persamaan linear:")
print(x)  # Menampilkan solusi
