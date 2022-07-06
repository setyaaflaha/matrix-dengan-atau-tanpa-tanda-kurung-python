import numpy as np
B = int(input("Masukan Jumlah Baris yang diinginkan = "))
K = int(input("Masukkan Jumlah Kolom yang diinginkan = "))
matrix = []
Tulis = "Matrix tanpa tanda kurung"
print ("Masukkan angka yang ingin dimasukan dalam matrix")

#Matrix Tanpa Tanda Kurung
for i in range(B):
    a =[]
    for j in range(K):    
            a.append(int(input()))
    matrix.append(a)
print (Tulis)
for i in range(B):
    for j in range(K):
        print(matrix[i][j], end = " ")
    print()
    
#Matrix dengan tanda kurung
print ("Matrix dengan tanda kurung")
entries = list(map(int, input().split()))
matrix1 = np.array(entries).reshape(B, K)
print(matrix1)